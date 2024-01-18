from odoo import models, fields, api
class ReportClient(models.Model):
    _name = 'report_client.report'


    client_id = fields.Many2one('res.partner', string='Client')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')


    def generate_report(self):
        # Fetch commands based on selected client and date range
        commands = self.env['sale.order'].search([
            ('partner_id', '=', self.client_id.id),
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date),
        ])

        # Prepare data to pass to the report template
        report_data = {
            'commands': commands,
            'client': self.client_id.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

        # Render the report using the QWeb template

        report_template = self.env.ref('report_client_report.command_report')  # Replace 'report_client.report_template_id' with the actual XML ID of your report template

        # Create an ir.actions.report instance
        report_action = report_template.report_action(self, data=report_data)

        return report_action