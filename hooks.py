# -*- coding: utf-8 -*-
"""Cross-repo M2M ref restoration.

To break install-time dep cycles, several base.automation records in
BugFix-Sales, BugFix-Stock, and BugFix-Accounting were shipped with their
`trigger_field_ids` / `on_change_field_ids` / `action_server_ids` M2M refs
cleared. Studio-Misc installs LAST (declares depends on all involved
modules), so this hook re-attaches the missing refs after every module in
the graph is present.

Idempotent: uses write with [(6, 0, ids)] which replaces the M2M contents
each run. Safe to re-run on module upgrade.
"""
import logging

_logger = logging.getLogger(__name__)

# (automation_xmlid, m2m_field_on_base_automation, [target_xmlid, ...])
RESTORATIONS = [
    ('BugFix-Sales.base_automation_163_sls_track_vat_registration_status_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_vat_registration_status']),
    ('BugFix-Sales.base_automation_164_sls_track_vat_registration_no_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_vat_registration_number']),
    ('BugFix-Sales.base_automation_165_sls_track_svat_registration_status_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_svat_registration_status']),
    ('BugFix-Sales.base_automation_166_sls_track_svat_registration_no_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_svat_registration_number']),
    ('BugFix-Sales.base_automation_168_sls_track_mandatory_bank_guarantee_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_mandatory_bank_guarantee']),
    ('BugFix-Sales.base_automation_180_sls_track_vat_exempted_number_in_customer',
     'trigger_field_ids',
     ['Fix-repair.field_res_partner__x_studio_vat_exempted_number']),
    ('BugFix-Sales.base_automation_316_jin_company_id_in_delivery_terms',
     'trigger_field_ids',
     ['BugFix-Purchase.field_x_delivery_terms__create_date']),
    ('BugFix-Stock.base_automation_124_srm_auto_populate_report_type_in_product_moves',
     'on_change_field_ids',
     ['BugFix-Accounting.field_x_sales_report_model__x_studio_as_on_date']),
    ('BugFix-Accounting.base_automation_289_jin_company_id_in_consignment_charge_header',
     'action_server_ids',
     ['BugFix-Stock.server_action_2617_jin_company_id_in_consignment_charge_header']),
]


def post_init_hook(env):
    for auto_xmlid, field_name, target_xmlids in RESTORATIONS:
        auto = env.ref(auto_xmlid, raise_if_not_found=False)
        if not auto:
            _logger.info('post_init_hook: %s not found — skip', auto_xmlid)
            continue
        target_ids = []
        for xid in target_xmlids:
            rec = env.ref(xid, raise_if_not_found=False)
            if rec:
                target_ids.append(rec.id)
            else:
                _logger.warning('post_init_hook: target %s not found for %s', xid, auto_xmlid)
        if target_ids:
            try:
                auto.write({field_name: [(6, 0, target_ids)]})
                _logger.info('post_init_hook: restored %s.%s = %s', auto_xmlid, field_name, target_xmlids)
            except Exception as e:
                _logger.warning('post_init_hook: %s restoration failed: %s', auto_xmlid, e)
