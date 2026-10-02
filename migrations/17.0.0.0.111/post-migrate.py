# -*- coding: utf-8 -*-
"""v17.0.0.0.111: repair next_activity server actions broken by the 15->17 migration.

Two failure modes, both on ir.actions.server with state='next_activity':

(1) activity_user_type='generic' with activity_user_field_name EMPTY.
    Odoo 17 mail/ir_actions_server._run_action_next_activity does
        `self.activity_user_field_name in record`
    -> `False in record` -> TypeError: unsupported operand types in:
       False in x_purchase_request(12,)
    Hit on the Purchase Request "Approve" button (action 3076).
    Target: 10 rows. CDB: 0 rows (every CDB generic action names a field).

(2) activity_user_type='specific' with activity_user_id EMPTY.
    mail.activity.user_id is required -> the "...Notify User" actions crash
    the moment they fire. Target: 25 rows. CDB: 0 rows (each has a real user).

Fix policy — CDB-faithful, keyed so it survives differing record ids:

  Generic -> field name, keyed by (model, action name). CDB value is
  'user_id' everywhere. For sale.order / account.move that field exists
  on target, so the exact CDB value is restored.
  DEVIATION (deliberate, flagged): x_purchase_request and x_material_request
  have NO user_id field on EITHER env — CDB's 'user_id' there was already a
  dead config that Odoo 15 silently tolerated. The only res.users field on
  both models on both envs is x_studio_requested_by ("Requested by"), which
  also matches the actions' intent ("Approve ... Confirm" notifies the
  requester). We use that. A missing field is never written: every
  candidate is checked against env[model]._fields first.

  Specific -> user, keyed by (model, action name) -> res.users.login.
  Logins are stable across envs; numeric ids are not (CDB Kapila=8,
  target Kapila=11). Resolved at runtime via search on login.

Idempotent: both passes only touch rows that are still empty.
ORM only, no cr.execute.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)
TAG = '[BugFix-Studio-Misc v111]'

# (model, action name) -> activity_user_field_name   [from CDB, see docstring]
GENERIC_FIELD = {
    ('sale.order',         'SLS - Bank Guarantee Approval - Confirm'):      'user_id',
    ('sale.order',         'SLS - Credit Limit Approval - Confirm'):        'user_id',
    ('sale.order',         'SLS - Margin Approval - Confirm'):              'user_id',
    ('sale.order',         'SLS - Over Commission Approval - Confirm'):     'user_id',
    ('sale.order',         'SLS - Overdue Request Approval - Notify User'): 'user_id',
    ('sale.order',         'SLS - Temporary Credit Approval - Confirm'):    'user_id',
    ('account.move',       'SLS - Credit Note Approval - Confirm'):         'user_id',
    # DEVIATION from CDB literal 'user_id' (field absent on both envs):
    ('x_purchase_request', 'Approve PR - Confirm'):                         'x_studio_requested_by',
    ('x_material_request', 'MR Request Approve Confirm - Notify User'):     'x_studio_requested_by',
}
# Ordered fallback for generic rows not in the map above.
GENERIC_FALLBACK = ('user_id', 'x_studio_requested_by')

# (model, action name) -> res.users.login   [from CDB]
SPECIFIC_LOGIN = {
    ('x_material_request',   'MR Request Approval - Notify User'):               'kapila.h@jinasena.com.lk',
    ('product.template',     'PLM - Item Approval - Notify  Project User'):      'kapila.h@jinasena.com.lk',
    ('product.template',     'PLM - Item Approval Request - Notify User'):       'kapila.h@jinasena.com.lk',
    ('product.product',      'PROJ - Item Approval - Notify  Project User'):     'kapila.h@jinasena.com.lk',
    ('product.product',      'PROJ - Item Approval Request - Notify User'):      'kapila.h@jinasena.com.lk',
    ('stock.picking',        'PROJ - Notify Transfer Completion'):               'janitha.r@jinasena.com.lk',
    ('sale.order',           'PROJ - Project Item Request Approval - Notify User'): 'kapila.h@jinasena.com.lk',
    ('project.update',       'PROJ - Project Update - Notify PM'):               'janitha.r@jinasena.com.lk',
    ('sale.order',           'RR - RUG Request Approval - Notify User'):         'janitha.r@jinasena.com.lk',
    ('sale.order',           'RR - Re-estimate Request - Notify User'):          'kapila.h@jinasena.com.lk',
    ('stock.picking',        'RR - Transfer Request Approval - Notify User'):    'kapila.h@jinasena.com.lk',
    ('x_purchase_request',   'Request Approval PR - Notify User'):               'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Bank Guarantee - Notify User'):              'janitha.r@jinasena.com.lk',
    ('sale.order',           'SLS - Margin Request Approval - Notify User'):     'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Over Commission Request Approval - Notify User'): 'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Overdue Request Approval - Notify User'):    'milinda.bakmiwewa@jinasena.com.lk',
    ('sale.order',           'SLS - Request Approval - Notify User'):            'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Request Bank Guarantee Approval - Notify User'): 'tharaka.h@jinasena.com.lk',
    ('account.move',         'SLS - Request Credit Note Approval - Notify User'): 'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Request Temporary Credit Approval - Notify User'): 'tharaka.h@jinasena.com.lk',
    ('sale.order',           'SLS - Send Bank Guarantee Notification - Confirm'): 'tharaka.h@jinasena.com.lk',
    ('x_sales_report_model', 'SRM - RPT - Project Gross Margin - Notify User'):  'rohana.b@jinasena.com.lk',
    ('account.account',      'TEST - For Rohana'):                               'kapila.h@jinasena.com.lk',
}


def _key(act):
    model = act.model_id.model if act.model_id else ''
    return (model, (act.name or '').strip())


def _lookup(mapping, key):
    """Exact match first; then prefix match on the action name (CDB names were
    truncated to 45 chars in the probe that produced these tables)."""
    if key in mapping:
        return mapping[key]
    model, name = key
    for (m, n), v in mapping.items():
        if m == model and (name.startswith(n) or n.startswith(name)):
            return v
    return None


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Action = env['ir.actions.server'].sudo()
    Users = env['res.users'].sudo()

    # ---- (1) generic: back-fill activity_user_field_name -------------------
    generic = Action.search([
        ('state', '=', 'next_activity'),
        ('activity_user_type', '=', 'generic'),
        '|', ('activity_user_field_name', '=', False), ('activity_user_field_name', '=', ''),
    ])
    g_fixed = 0
    for act in generic:
        key = _key(act)
        model = key[0]
        if model not in env:
            _logger.warning('%s generic id=%s %r: model %r not in registry, skip', TAG, act.id, act.name, model)
            continue
        fields = env[model]._fields
        candidates = []
        mapped = _lookup(GENERIC_FIELD, key)
        if mapped:
            candidates.append(mapped)
        candidates += [f for f in GENERIC_FALLBACK if f not in candidates]
        chosen = next((f for f in candidates if f in fields), None)
        if not chosen:
            _logger.warning('%s generic id=%s %r on %s: none of %s exist, left empty',
                            TAG, act.id, act.name, model, candidates)
            continue
        act.activity_user_field_name = chosen
        g_fixed += 1
        note = '' if chosen == (mapped or chosen) else ' (fallback)'
        _logger.info('%s generic id=%s %r on %s: activity_user_field_name <- %r%s',
                     TAG, act.id, act.name, model, chosen, note)
    _logger.info('%s generic: fixed %d / %d', TAG, g_fixed, len(generic))

    # ---- (2) specific: back-fill activity_user_id via login -----------------
    specific = Action.search([
        ('state', '=', 'next_activity'),
        ('activity_user_type', '=', 'specific'),
        ('activity_user_id', '=', False),
    ])
    s_fixed = 0
    login_cache = {}
    for act in specific:
        key = _key(act)
        login = _lookup(SPECIFIC_LOGIN, key)
        if not login:
            _logger.warning('%s specific id=%s %r on %s: no CDB login mapping, left empty',
                            TAG, act.id, act.name, key[0])
            continue
        if login not in login_cache:
            login_cache[login] = Users.with_context(active_test=False).search(
                [('login', '=', login)], limit=1)
        user = login_cache[login]
        if not user:
            _logger.warning('%s specific id=%s %r: login %r not found on this env, left empty',
                            TAG, act.id, act.name, login)
            continue
        act.activity_user_id = user.id
        s_fixed += 1
        _logger.info('%s specific id=%s %r on %s: activity_user_id <- %s (%s)',
                     TAG, act.id, act.name, key[0], user.id, login)
    _logger.info('%s specific: fixed %d / %d', TAG, s_fixed, len(specific))
