

from odoo import models, fields, api
from num2words import num2words
import re

#  code for print
class ProductTemplate(models.Model):
    _inherit = 'product.product'

    Arrondi = fields.Boolean(string='Arrondi', default=False)

# end code section



class PurchaseOrderLine(models.Model):
        _inherit = "purchase.order.line"

        vehicle_id = fields.Many2one('fleet.vehicle', string='Véhicule')
        
        


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

  
        
    @api.depends('amount_total')
    def amount_to_words(self):
        
        self.amount_in_words= num2words(self.amount_total,lang='fr')

    objet = fields.Html(string='Objet')    
    amount_in_words = fields.Char(string='Amount in Words', compute='amount_to_words')    

    moyen_transport = fields.Many2one('fleet.vehicle', string='Moyen de transport')
    charge = fields.Float(string='Charge',related='moyen_transport.charge')
    volume = fields.Float(string='Volume',related='moyen_transport.volume')
    conducteur = fields.Many2one('res.partner',string='Conducteur',compute="get_conducteur", store=True,inverse="set_conducteur")


    @api.depends('moyen_transport')
    def get_conducteur(self):
        for rec in self:
            if rec.moyen_transport:

                vehicle_id = self.env['fleet.vehicle'].search([('id', '=', rec.moyen_transport.id)])

                rec.conducteur = vehicle_id.driver_id
            else:
                rec.conducteur = None

    def set_conducteur(self):
        for purchase in self:
            if not (purchase.moyen_transport):
                continue

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            for line in order.order_line:
                for move in line.move_ids:
                    move.write({'vehicle_id': line.vehicle_id.id})
            stock_move_vals = {
                'moyen_transport': order.moyen_transport.id,
                'charge': order.charge,
                'volume': order.volume,
                'conducteur': order.conducteur.id,
               
            }
            # Iterate through related pickings and update the values
            for picking in order.picking_ids:
                picking.write(stock_move_vals)
        return res

    def action_create_invoice(self):
        res = super(PurchaseOrder, self).action_create_invoice()
        if res.get('res_id'):
            invoice = self.env['account.move'].browse(res['res_id'])
            for line in invoice.invoice_line_ids:
                if line.purchase_line_id:
                    line.write({
                        'vehicle_id': line.purchase_line_id.vehicle_id.id,
                        
                    })
            invoice.write({'objet':self.objet,})
        return res

class StockMove(models.Model):
    _inherit = 'stock.move'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Véhicule')
    kilometrage=fields.Float(string='Kilométrage')
    #employe_liste = fields.Many2one('hr.employee', string='Employé')
    #linked_employe = fields.Selection(related='product_id.categ_id.employe')

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    moyen_transport = fields.Many2one('fleet.vehicle', string='Moyen de transport')#,compute='_get_moyen_transport', store=True,inverse='set_moyen_transport'
    charge = fields.Float(string='Charge',related='moyen_transport.charge')
    volume = fields.Float(string='Volume',related='moyen_transport.volume')
    conducteur = fields.Many2one('res.partner', string='Conducteur')
    bl_fournisseur = fields.Char(string='BL fournisseur')
    nombre_voyage= fields.Float(string='Nombre de voyage',default=1)

    @api.onchange('nombre_voyage')
    def onchange_nombre_de_voyage(self):
        if self.nombre_voyage:
           for rec in self.move_ids_without_package:
               rec.quantity_done = self.nombre_voyage * self.volume

        
    """
    @api.depends('sale_id')    
    def _get_moyen_transport(self): 
        for rec in self:
            rec.moyen_transport=sale_id.moyen_transport.id

    def set_moyen_transport(self):
        for rec in self:
            if not (rec.sale_id):
                continue    
            
    """    
    """
    @api.onchange('moyen_transport')    
    def _get_volume(self):
        for order in self:
            vehicle_id=self.env['fleet.vehicle'].search([('id', '=', order.moyen_transport.id)],limit=1)
            if len(vehicle_id)>0:
                 
                order.volume = vehicle_id.volume
               
            else:
                continue
                    
    @api.onchange('moyen_transport')    
    def _get_charge(self):
        for order in self:
            vehicle_id=self.env['fleet.vehicle'].search([('id', '=', order.moyen_transport.id)],limit=1)
            if len(vehicle_id)>0:
                order.charge = vehicle_id.charge 
                       
            else:
                continue                
        
    """
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Véhicule')

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    charge=fields.Float(string='Charge')
    volume = fields.Float(string='Volume')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    objet = fields.Html(string='Objet')
    moyen_transport = fields.Many2one('fleet.vehicle', string='Moyen de transport')
    charge = fields.Float(string='Charge', related='moyen_transport.charge')
    volume = fields.Float(string='Volume', related='moyen_transport.volume')
    conducteur = fields.Many2one('res.partner', string='Conducteur', compute="get_conducteur", store=True,inverse="set_conducteur")
    amount_in_words = fields.Char(string='Amount in Words', compute='amount_to_words') 
        
    @api.depends('amount_total')
    def amount_to_words(self):
        
        self.amount_in_words= num2words(self.amount_total,lang='fr')

    @api.depends('user_id', 'company_id')
    def _compute_warehouse_id(self):
        for order in self:
            default_warehouse_id = self.env['ir.default'].with_company(
                order.company_id.id).get_model_defaults('sale.order').get('warehouse_id')

            if order.state in ['draft', 'sent'] or not order.ids:
                order.warehouse_id = None
            else:
                if default_warehouse_id is not None:
                    order.warehouse_id = default_warehouse_id
                else:
                    order.warehouse_id = order.user_id.with_company(order.company_id.id)._get_default_warehouse_id() 
                        
    @api.depends('moyen_transport')
    def get_conducteur(self):
        for rec in self:
            if rec.moyen_transport:

                vehicle_id = self.env['fleet.vehicle'].search([('id', '=', rec.moyen_transport.id)])

                rec.conducteur = vehicle_id.driver_id
            else:
                rec.conducteur = None


    def set_conducteur(self):
        for purchase in self:
            if not (purchase.moyen_transport):
                continue



    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for picking in order.picking_ids:
                picking.write({
                    'moyen_transport': order.moyen_transport.id,
                    #'charge': order.charge,
                    #'volume': order.volume,
                    'conducteur': order.conducteur.id,
                     
                })
        return res
            
    def _prepare_invoice(self):
       
        res = super(SaleOrder, self)._prepare_invoice()

        res.update({
            'objet': self.objet,  
          
        })

        return res        

    
            
class AccountMove(models.Model):
    _inherit = 'account.move'

    objet = fields.Html(string='Objet')
    amount_in_words = fields.Char(string='Amount in Words', compute='amount_to_words') 
        
    @api.depends('amount_total')
    def amount_to_words(self):
        
        self.amount_in_words= num2words(self.amount_total,lang='fr')
    


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    moyen_transport = fields.Many2one('fleet.vehicle', string='Moyen de transport')
    charge = fields.Float(string='Charge')
    volume = fields.Float(string='Volume')
    conducteur = fields.Many2one('res.partner', string='Conducteur')
        
