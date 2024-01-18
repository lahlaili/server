from odoo import models, fields, api

class InfoAdditionel(models.Model):
    _name = "info.additionel"

    client_id = fields.Many2one("res.partner", "Client", default=lambda self: self.env.context.get('client_id'))
    annee = fields.Integer('annee')
    ca = fields.Float('CA')
    effectif = fields.Integer("Effectif de l'entreprise")
    cadres = fields.Integer("Cadres")
    employes = fields.Integer("Employer")
    ouvriers = fields.Integer("Ouvriers")

class ResPartner(models.Model):
    _inherit = 'res.partner'
    info_additional_ids = fields.One2many('info.additionel', 'client_id', string='info additional ids')

    def open_info_additional_view(self):
        return {
            'name': 'additional',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'info.additionel',
            'context': {'client_id': self.id},
            'domain': [('client_id', '=', self.id)]
        }
