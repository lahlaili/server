from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'tee'
    _description = 'Description'

    name = fields.Char(string="Name")
    date=fields.Date(string="Date de commande")
    description=fields.Text(string="Descrition")
