# -*- coding: utf-8 -*-
from odoo import models, fields

class X_website_faqs(models.Model):
    _name = 'x_website_faqs'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'website FAQs'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Description', required=True, translate=True)
    x_studio_active = fields.Boolean(string='Active')
    x_studio_answer = fields.Char(string='Answer')
    x_studio_boolean_field_1ap_1iph4t6ob = fields.Boolean(string='New CheckBox')
    x_studio_question = fields.Char(string='Question')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_website_description = fields.Html(string='Website Description')
    x_studio_website_published = fields.Boolean(string='Website Published')
