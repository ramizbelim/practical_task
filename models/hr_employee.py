from odoo import models, fields

class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"

    hours_assigned = fields.Float(string="H.Assigned")
