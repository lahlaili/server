# models.py

from odoo import models, fields, api


class ClientOrderReport(models.Model):
    _name = 'client.order.report'
    _description = 'Client Order Report'

    client_id = fields.Many2one('res.partner', string='Client')
    order_ids = fields.Many2many('sale.order', string='Orders')

    @api.model
    def get_report_data(self, client_id):
        client = self.env['res.partner'].browse(client_id)
        orders = self.env['sale.order'].search([('partner_id', '=', client_id)])

        return {
            'client': client,
            'orders': orders,
        }
