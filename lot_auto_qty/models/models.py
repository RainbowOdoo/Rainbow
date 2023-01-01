# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class InheritStockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.onchange('qty_done')
    def _onchange_qty_done(self):
        for line in self:
            if not self.env.context.get('form_view_ref'):
                if line.qty_done > line.lot_id.product_qty:
                    raise UserError(
                        _(f"You are exceeding from Lot Quantity,  Maximum Lot quantity is {line.lot_id.product_qty}"))

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        for line in self:
            if not self.env.context.get('form_view_ref'):
                line.qty_done = line.lot_id.product_qty
