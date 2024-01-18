from odoo import models, fields, api

class CustumCrm(models.Model):
    _inherit = 'crm.lead'


    date_consultation = fields.Date(string="Date de consultation", default=lambda self: fields.Date.today())
    source = fields.Selection(selection=[('source1', 'Source 1'), ('source2', 'Source 2')], string="Source",default='')
    type_demande = fields.Selection(selection=[('type1', 'Type 1'), ('type2', 'Type 2')], string="Type de la demande",default='')

    demandeur = fields.Many2one('res.partner', string="Demandeur", domain="[('parent_id', '=', partner_id)]")

    email_demandeur = fields.Char(string="Email demandeur", related='demandeur.email', readonly=True)
    telephone_demandeur = fields.Char(string="Téléphone demandeur", related='demandeur.phone', readonly=True)
    secteur_activite = fields.Many2one('res.partner.industry', string="Secteur d'activité",related='demandeur.industry_id', readonly=True)

class Visite(models.Model):
    _name = 'crm_custum.visite'
    _description = 'Visite Model'

    date = fields.Date(string="Date" )
    type = fields.Selection([
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ], string="Type")
