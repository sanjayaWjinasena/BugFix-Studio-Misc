# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Studio-Misc',
    'version': '17.0.0.0.1',
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
    # Depends kept minimal so this module can absorb x_* models
    # regardless of which domain they touch. Additional module deps
    # will be added when specific ports need them.
    'depends': [
        'base_setup',
        'base_automation',   # for usage='base_automation' selection value
        'mail',              # for _inherit=['mail.thread','mail.activity.mixin']
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # Data files land here as ports are shipped (Phase 3.12).
        # 'data/server_actions.xml',
        # 'data/base_automations.xml',
        # 'data/window_actions.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
