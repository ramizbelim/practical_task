from odoo import models, fields,api

class ProjectPlanningLine(models.Model):
    _name = "project.planning.line"

    project_id = fields.Many2one("project.project", string="Project")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    hours_invested = fields.Float(string='H.Invested', compute='_compute_hours_invested',
                                  store=True, readonly=False)
    hours_assigned = fields.Float('H.Assigned')
    hours_assigned_string = fields.Char(string='H.Assigned')
    hour_pending = fields.Float('H.Pending')
    hours_pending_string = fields.Char(string="H.Pending")

    @api.depends('project_id', 'employee_id')
    def _compute_hours_invested(self):
        unit_amountssss = self.env["account.analytic.line"].search([('name', '=', 'project_id.display_name')])
        # print("===========",self.project_id.timesheet_ids.unit_amount)
        print("===========",unit_amountssss)
        # self.hours_assigned = self.project_id.timesheet_ids.unit_amount
