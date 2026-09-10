# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Studio-Misc',
    'version': '17.0.0.0.42',
    'summary': (
        'Catch-all landing zone for Studio-created artefacts that '
        'don\'t fit any of the domain-specific companion modules '
        '(BugFix-Sales, BugFix-Purchase, BugFix-Accounting, BugFix-Stock, '
        'BugFix-MRP, BugFix-HR, BugFix-Project, BugFix-Maintenance, '
        'BugFix-Analytics, Fix-repair, Jinasena_Masterdata_Reporting).'
    ),
    'description': """
Studio-Misc Landing Zone
========================

Created 2026-09-07 as part of the routing audit for the remaining
~4,261 unported Studio artefacts. Serves as the owning module for:

* orphan ``x_*`` custom models that don't belong to a specific
  domain (test/scratch models like ``x_test02``, ``x_website_faq*``,
  ``x_sales_model_debug``, etc.)
* small standard-Odoo Studio-touched buckets that don't warrant
  their own repo (``crm.*``, ``quality.*``, ``loyalty.*``,
  ``pos.*``, ``delivery.carrier``, etc.)
* ``ir.sequence`` records without a target-model context
* ``ir.ui.menu`` records without a routable action

The alternative was creating 15+ tiny per-domain modules — this
consolidates them into one landing zone with clear scope.

Ports land in ``data/`` and ``views/`` subdirectories, one file per
category (server_actions.xml, base_automations.xml, window_actions.xml,
etc.).
""",
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    # v17.0.0.0.3: widen depends to unblock Studio backlog port.
    # Progress audit confirmed all 20 blocking addons are already
    # installed on target — no risk of pulling in unwanted modules.
    # Enables porting artefacts on crm.lead / calendar.event /
    # loyalty.* / pos.* / website.* / stock.* / sale.* / account.*.
    'depends': [
        'base_setup',
        'base_automation',
        'mail',
        'hr_expense',
        'documents_hr_expense',
        'helpdesk',
        'purchase_requisition',
        'mrp_plm',
        'mrp_landed_costs',
        'stock_landed_costs',
        'account_edi',
        'industry_fsm_sale',
        'hr_attendance',
        'project',
        'crm',
        'seed_master_data_and_settings',  # for company_id refs
        'sale_crm',
        'sales_team',
        'calendar',
        'loyalty',
        'point_of_sale',
        'pos_sale',
        'pos_loyalty',
        'pos_mercury',
        'pos_restaurant',
        'pos_restaurant_appointment',
        'pos_online_payment',
        'website',
        'website_sale',
        'website_sale_loyalty',
        'delivery',
        'stock',
        'sale',
        'purchase',
        'account',
    ],
    'data': [
        'data/rules_f7.xml',
        'data/menus_f6.xml',
        'data/server_actions_f5.xml',
        # Security first so record rules can ref groups declared upstream.
        'security/ir.model.access.csv',
        # Data files land here as ports are shipped (Phase 3.12).
        'data/server_actions_backlog.xml',
        'data/window_actions_backlog.xml',
        'data/record_rules.xml',
        'data/sequences.xml',
        'data/menus_website_faq.xml',
        'data/menus_from_routing.xml',
        'views/calendar_filters_views.xml',
        'views/x_product_product_views.xml',
        'views/x_product_test_views.xml',
        'views/x_test02_views.xml',
        'views/x_test_1_views.xml',
        'views/x_test_form_views.xml',
        'views/x_test_layout_views.xml',
        'views/x_test_model_link_2_views.xml',
        'views/x_test_model_link_views.xml',
        'views/x_test_model_primary_views.xml',
        'views/x_testapp_views.xml',
        'views/x_testdepartment_views.xml',
        'views/x_website_faq_views.xml',
        'views/x_website_faqs_views.xml',
        'views/crm_team_ext_views.xml',
        'views/crm_team_member_ext_views.xml',
        'views/res_currency_ext_views.xml',
        'views/x_product_test_ext_views.xml',
        'views/x_test02_ext_views.xml',
        'views/x_test_1_ext_views.xml',
        'views/x_test_form_ext_views.xml',
        'views/x_test_layout_ext_views.xml',
        'views/x_test_model_link_2_ext_views.xml',
        'views/x_test_model_link_ext_views.xml',
        'views/x_test_model_primary_ext_views.xml',
        'views/x_testdepartment_ext_views.xml',
        'views/x_website_faq_ext_views.xml',
        'views/x_website_faqs_ext_views.xml',
        'views/qweb_faq_views.xml',
        'data/gap_automations.xml',
        'data/record_rules_gap.xml',
        'data/server_actions_gap.xml',
        'data/automations_gap.xml',
        'data/window_actions_gap.xml',
        'data/ir_defaults_ported.xml',
        'data/report_templates.xml',
        'data/report_actions.xml',
        'data/server_actions_d7.xml',
        'data/window_actions_d7.xml',
        'data/automations_d7.xml',
        'data/menus_d5.xml',
        'views/x_bve_salesreport_e_views.xml',
        'views/x_bve_samplebalancemovementreport_e_views.xml',
        'views/x_bve_test1_e_views.xml',
        'views/x_custom_reports_line_c55e7_e_views.xml',
        'views/x_custom_reports_tag_e_views.xml',
        'views/x_customer_groups_e_views.xml',
        'views/x_material_request_mt_line_9a011_e_views.xml',
        'views/x_material_request_tes_line_3301b_e_views.xml',
        'views/x_project_task_worksheet_template_1_e_views.xml',
        'views/x_res_config_settings_e_views.xml',
        'views/x_sales_model_debug_e_views.xml',
        'views/x_test02_e_views.xml',
        'views/x_work_center_costing_e_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
