from odoo import models, fields,api

class ProjectPlanningLine(models.Model):
    _name = "project.planning.line"

    project_id = fields.Many2one("project.project", string="Project")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    hours_invested = fields.Float(string='H.Invested', compute='_compute_hours_invested',
                                  store=True, readonly=False)
    hours_assigned = fields.Float('H.Assigned')
    hours_assigned_string = fields.Char(string='H.Assigned')
    hour_pending = fields.Float('H.Pending', compute="_compute_hour_pending", store=True, readonly=False)
    hours_pending_string = fields.Char(string="H.Pending")

    @api.depends('employee_id')
    def _compute_hours_invested(self):
        total_hours_invested = 0
        for rec in self.project_id.timesheet_ids:
            if rec.project_id.display_name == self.project_id.display_name:
                if self.employee_id.name == rec.employee_id.name:
                    print("************",rec.unit_amount)
                    total_hours_invested += rec.unit_amount
        self.hours_invested = total_hours_invested




    @api.onchange('employee_id')
    def _onchange_hours_assigned(self):
        self.hours_assigned = self.employee_id.hours_assigned
        self.hours_assigned_string = f"{self.hours_assigned}/{self.hours_invested}"

    @api.depends('hour_pending')
    def _compute_hour_pending(self):
        self.hour_pending = self.hours_invested - self.hours_assigned
        if self.hours_assigned > self.hours_invested:
            self.hours_pending_string = 0.0
        else:
            self.hours_pending_string = f"{self.hour_pending}/{self.hours_invested}"
