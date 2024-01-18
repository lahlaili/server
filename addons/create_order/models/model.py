from odoo import models,fields

class CreateOrder(models.Model):
    _name="create_order"

    def order_create(self):
        self.env['res.partner'].create({
            "name":"Ezzahti116",
            "email":"ezzahtimomed13",
            "child_ids":1,
            "parent_name":"Zahtot",
            "parent_id":25
        })







