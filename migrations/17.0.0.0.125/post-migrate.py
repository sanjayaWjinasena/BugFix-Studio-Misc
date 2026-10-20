# -*- coding: utf-8 -*-
"""v0.0.125: Divisional P&L menu opens its report again.

Clear-DB: Accounting/Reporting/Divisional P&L (Studio menu) opens a client
action (tag account_report, context {'report_id': <id>}) on the hand-made
account.report "Divisional P&L". The port shipped the menu with no parent and
no action, so it showed nowhere. The parent now comes from
data/menus_studio_gap.xml; the report and its action are environment data with
no xmlid, so the action is found here by its report (never by a numeric id).

ORM only. Idempotent: no-op when the report is absent (fresh installs) and when
the menu already points at the right action. Reuses the existing client action
when one exists; creates one only if none does.
"""
import ast
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

REPORT_NAME = 'Divisional P&L'
MENU_XMLID = 'BugFix-Studio-Misc.menu_studio_divisional_pl'


def _report_id_of(action):
    try:
        return (ast.literal_eval(action.context or '{}') or {}).get('report_id')
    except Exception:
        return None


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
    menu = env.ref(MENU_XMLID, raise_if_not_found=False)
    if not menu:
        _logger.info('Divisional P&L: menu %s not found, skip', MENU_XMLID)
        return
    report = env['account.report'].search([('name', '=', REPORT_NAME)], limit=1)
    if not report:
        _logger.info('Divisional P&L: no account.report named %r here, menu left without action', REPORT_NAME)
        return
    actions = env['ir.actions.client'].search([('tag', '=', 'account_report')])
    action = actions.filtered(lambda a: _report_id_of(a) == report.id)[:1]
    if not action:
        action = env['ir.actions.client'].create({
            'name': REPORT_NAME,
            'tag': 'account_report',
            'context': repr({'report_id': report.id}),
        })
        _logger.info('Divisional P&L: created client action %s for report %s', action.id, report.id)
    if menu.action != action:
        menu.action = action
        _logger.info('Divisional P&L: menu %s now opens action %s (report %s)', menu.id, action.id, report.id)
