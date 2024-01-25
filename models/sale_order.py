from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    shipping_hold = fields.Boolean("Shipping Hold")


    def action_confirm(self):
        res=super(SaleOrder, self).action_confirm()
        picking_record_id = self.env["stock.picking"].search([("origin" ,"=",self.name)])
        if self.shipping_hold == True :
            if picking_record_id.state != 'done':
                picking_record_id.shipping_hold = True
        return res
    @api.onchange('shipping_hold')
    def _onchange_shipping_hold(self):
        picking_record_id = self.env["stock.picking"].search([("origin" ,"=",self.name)])
        if self.shipping_hold == False:
            if picking_record_id.state != 'done':
                picking_record_id.shipping_hold = False
        if self.shipping_hold == True:
            picking_record_id.shipping_hold = True





