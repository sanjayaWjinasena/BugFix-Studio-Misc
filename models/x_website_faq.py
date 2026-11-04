from odoo import fields, models


class X_website_faq(models.Model):
    _name = "x_website_faq"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "website.faq"

    active = fields.Boolean(string="Active")
    x_faqfield = fields.Text(string="FAQ", readonly=True)
    name = fields.Char(string="Description", required=True, translate=True)
    x_studio_answer = fields.Char(string="Answer")
    x_studio_char_field_c3_1ipgu110c = fields.Char(string="New Text")
    x_studio_published_on_the_website = fields.Boolean(
        string="published on the website"
    )
    x_studio_question = fields.Char(string="Question")
    sequence = fields.Integer(string="Sequence")


class XWebsiteFaqGap(models.Model):
    _inherit = "x_website_faq"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    x_faqfield = fields.Text(string="FAQ", readonly=True)
    name = fields.Char(string="Description", required=True)
