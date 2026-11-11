from odoo import fields, models


class X_website_faq(models.Model):
    _name = "website_faq"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "website.faq"

    active = fields.Boolean()
    faqfield = fields.Text(string="FAQ", readonly=True)
    name = fields.Char(string="Description", required=True, translate=True)
    answer = fields.Char()
    char_field_c3_1ipgu110c = fields.Char(string="New Text")
    published_on_the_website = fields.Boolean(string="published on the website")
    question = fields.Char()
    sequence = fields.Integer()


class XWebsiteFaqGap(models.Model):
    _inherit = "website_faq"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    faqfield = fields.Text(string="FAQ", readonly=True)
    name = fields.Char(string="Description", required=True)
