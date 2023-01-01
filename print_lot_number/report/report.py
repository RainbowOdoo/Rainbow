from odoo import models


class LotReportPrint(models.AbstractModel):
    _name = 'report.print_lot_number.print_lot_number'
    _description = 'Print Lot Number'

    def _get_report_values(self, docids, data=None):
        return {
            'doc_model': 'account.move.line',
            'docs': self.env['account.move.line'].browse(1),
            'data': data['data'],
        }
