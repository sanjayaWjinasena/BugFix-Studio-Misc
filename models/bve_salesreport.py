from odoo import fields, models


class XBveSalesreport(models.Model):
    _name = "bve.salesreport"
    _description = "Sales Report"

    bve_t1_currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency", readonly=True
    )
    bve_t1_invoice_status = fields.Selection(
        selection=[
            ("upselling", "Upselling Opportunity"),
            ("invoiced", "Fully Invoiced"),
            ("to invoice", "To Invoice"),
            ("no", "Nothing to Invoice"),
        ],
        string="Invoice Status",
        readonly=True,
    )
    bve_t1_partner_id = fields.Many2one(
        comodel_name="res.partner", string="Customer", readonly=True
    )
    bve_t1_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist", string="Pricelist", readonly=True
    )
    bve_t1_team_id = fields.Many2one(
        comodel_name="crm.team", string="Sales Team", readonly=True
    )
    bve_t1_user_id = fields.Many2one(
        comodel_name="res.users", string="Salesperson", readonly=True
    )
    bve_t1_warehouse_id = fields.Many2one(
        comodel_name="stock.warehouse", string="Warehouse", readonly=True
    )
    bve_t1_customer_credit_limit = fields.Float(
        string="Customer Credit Limit", readonly=True
    )
    bve_t1_total = fields.Char(string="Total", readonly=True)
    bve_t2_product_id = fields.Many2one(
        comodel_name="product.product", string="Product", readonly=True
    )
    bve_t2_product_uom_qty = fields.Float(string="Quantity", readonly=True)
    bve_t2_qty_delivered = fields.Float(string="Delivery Quantity", readonly=True)


class XBveSalesreportGap(models.Model):
    _inherit = "bve.salesreport"

    bve_t1_currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency", readonly=True
    )
    bve_t1_invoice_status = fields.Selection(
        selection=[
            ("upselling", "Upselling Opportunity"),
            ("invoiced", "Fully Invoiced"),
            ("to invoice", "To Invoice"),
            ("no", "Nothing to Invoice"),
        ],
        string="Invoice Status",
        readonly=True,
    )
    bve_t1_partner_id = fields.Many2one(
        comodel_name="res.partner", string="Customer", readonly=True
    )
    bve_t1_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist", string="Pricelist", readonly=True
    )
    bve_t1_team_id = fields.Many2one(
        comodel_name="crm.team", string="Sales Team", readonly=True
    )
    bve_t1_user_id = fields.Many2one(
        comodel_name="res.users", string="Salesperson", readonly=True
    )
    bve_t1_warehouse_id = fields.Many2one(
        comodel_name="stock.warehouse", string="Warehouse", readonly=True
    )
    bve_t2_product_id = fields.Many2one(
        comodel_name="product.product", string="Product", readonly=True
    )
    bve_t2_product_uom_qty = fields.Float(string="Quantity", readonly=True)
    bve_t2_qty_delivered = fields.Float(string="Delivery Quantity", readonly=True)
