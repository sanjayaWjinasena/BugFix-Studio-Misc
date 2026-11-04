from odoo import fields, models


class XProjectTaskWorksheetTemplate1(models.Model):
    _name = "x_project_task_worksheet_template_1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Default Worksheet"

    x_comments = fields.Text(string="Comments")
    name = fields.Char(string="Name", related="x_project_task_id.name")
    x_project_task_id = fields.Many2one(
        comodel_name="project.task", string="Task", required=True, ondelete="cascade"
    )
