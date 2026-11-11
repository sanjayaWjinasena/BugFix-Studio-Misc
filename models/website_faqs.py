from odoo import fields, models


class X_website_faqs(models.Model):
    _name = "website_faqs"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "website FAQs"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Description", required=True, translate=True)
    accounting_active = fields.Boolean(string="Active")
    answer = fields.Char(string="Answer")
    boolean_field_1ap_1iph4t6ob = fields.Boolean(string="New CheckBox")
    question = fields.Char(string="Question")
    sequence = fields.Integer(string="Sequence")
    website_description = fields.Html(string="Website Description")
    website_published = fields.Boolean(string="Website Published")


class XWebsiteFaqsGap(models.Model):
    _inherit = "website_faqs"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Description", required=True)
