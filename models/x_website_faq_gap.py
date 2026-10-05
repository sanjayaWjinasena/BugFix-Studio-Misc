# -*- coding: utf-8 -*-
from odoo import models, fields

class XWebsiteFaqGap(models.Model):
    _inherit = 'x_website_faq'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_faqfield = fields.Text(string='FAQ', readonly=True)
    x_name = fields.Char(string='Description', required=True)
