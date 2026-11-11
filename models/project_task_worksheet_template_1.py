from odoo import fields, models


class XProjectTaskWorksheetTemplate1(models.Model):
    _name = "project_task_worksheet_template_1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Default Worksheet"

    comments = fields.Text()
    name = fields.Char(string="Name", related="project_task_id.name")
    project_task_id = fields.Many2one(
        comodel_name="project.task", string="Task", required=True, ondelete="cascade"
    )
