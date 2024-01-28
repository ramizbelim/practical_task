from odoo import models, fields, api
from datetime import date


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def write(self, vals):
        record =self.order_id
        if "price_unit" in vals:
            record.message_post(
                body=f'{record.user_id.name} updated the Unit price for {self.product_id.name} to {vals["price_unit"]}')
        return super().write(vals)