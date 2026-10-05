# -*- coding: utf-8 -*-
from odoo import models, fields

class XProjectTaskWorksheetTemplate1Gap(models.Model):
    _inherit = 'x_project_task_worksheet_template_1'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_comments = fields.Text(string='Comments')
    x_name = fields.Char(string='Name', related='x_project_task_id.name')
    x_project_task_id = fields.Many2one(comodel_name='project.task', string='Task', required=True)
