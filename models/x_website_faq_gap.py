# -*- coding: utf-8 -*-
from odoo import models, fields

class XWebsiteFaqGap(models.Model):
    _inherit = 'x_website_faq'

    x_active = fields.Boolean(string='Active')
    x_faqfield = fields.Text(string='FAQ', readonly=True)
    x_name = fields.Char(string='Description', required=True)
