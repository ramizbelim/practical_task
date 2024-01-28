from odoo import models, fields,api

class Project(models.Model):
    _inherit = "project.project"

    hours_total = fields.Float(string="Hours Project")
    hours_total_planned = fields.Float(string="Scheduled Hours", compute="_compute_hours_total_planned",
                                       store=True, readonly=False)
    planning_line_ids = fields.One2many(comodel_name ='project.planning.line',
                                        inverse_name='project_id',
                                        string="Planning Hours")

    @api.depends('hours_total','planning_line_ids.hours_invested')
    def _compute_hours_total_planned(self):
        sum_hours_invested = 0
        for rec in self.planning_line_ids:
            sum_hours_invested += rec.hours_invested
        self.hours_total_planned = self.hours_total - sum_hours_invested






