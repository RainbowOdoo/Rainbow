from odoo import api, fields, models


class InheritStockMove(models.Model):
    _inherit = 'stock.move'

    def print_report(self):
        recs = []
        picking_rec = self.env['stock.picking'].browse(self.env.context.get('default_picking_id'))
        for rec in self.move_line_nosuggest_ids:
            recs.append({
                'supplier': picking_rec.partner_id.name,
                'date': picking_rec.date_done,
                'good_received': picking_rec.name,
                'product_name': self.product_id.name,
                'picking_name': rec.picking_id.name,
                'lot_number': rec.lot_id.name,
                'lot_name': rec.lot_name,
                'gross_weight': rec.gross_weight,
                'tare': rec.tare,
                'net_weight': rec.qty_done,
                'barcode': self.product_id.barcode,
            })
        data = {'data': recs}
        return self.env.ref('print_lot_number.print_lot_number_id').report_action(self, data=data)
