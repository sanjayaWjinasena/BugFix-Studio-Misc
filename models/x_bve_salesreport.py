# -*- coding: utf-8 -*-
from odoo import models, fields

class XBveSalesreport(models.Model):
    _name = 'x_bve.salesreport'
    _description = 'Sales Report'

    x_bve_t1_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', readonly=True)
    x_bve_t1_invoice_status = fields.Selection(selection=[('upselling', 'Upselling Opportunity'), ('invoiced', 'Fully Invoiced'), ('to invoice', 'To Invoice'), ('no', 'Nothing to Invoice')], string='Invoice Status', readonly=True)
    x_bve_t1_partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', readonly=True)
    x_bve_t1_pricelist_id = fields.Many2one(comodel_name='product.pricelist', string='Pricelist', readonly=True)
    x_bve_t1_team_id = fields.Many2one(comodel_name='crm.team', string='Sales Team', readonly=True)
    x_bve_t1_user_id = fields.Many2one(comodel_name='res.users', string='Salesperson', readonly=True)
    x_bve_t1_warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string='Warehouse', readonly=True)
    x_bve_t1_x_studio_customer_credit_limit = fields.Float(string='Customer Credit Limit', readonly=True)
    x_bve_t1_x_studio_total = fields.Char(string='Total', readonly=True)
    x_bve_t2_product_id = fields.Many2one(comodel_name='product.product', string='Product', readonly=True)
    x_bve_t2_product_uom_qty = fields.Float(string='Quantity', readonly=True)
    x_bve_t2_qty_delivered = fields.Float(string='Delivery Quantity', readonly=True)
