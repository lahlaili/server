
from odoo import models, fields, api
from num2words import num2words
import re
class ResPartner(models.Model):
    _inherit = 'res.partner'

    rc = fields.Char(string='R.C.')
    tp = fields.Char(string='T.P.')
    iff = fields.Char(string='I.F.')
    cnss = fields.Char(string='C.N.S.S.')
    ice = fields.Char(string='I.C.E.')
    capital = fields.Char(string='Capital')


class ResCompany(models.Model):
    _inherit = 'res.company'

    rc = fields.Char(string='R.C.')
    tp = fields.Char(string='T.P.')
    iff = fields.Char(string='I.F.')
    cnss = fields.Char(string='C.N.S.S.')
    ice = fields.Char(string='I.C.E.')
    capital = fields.Char(string='Capital')

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.depends('tax_totals')
    def _compute_amount_in_words(self):
        for record in self:
            if 'formatted_amount_total' in record.tax_totals:
                # Remove currency symbols and commas, handle French number formatting
                amount_cleaned = re.sub(r'[^\d,]', '', record.tax_totals['formatted_amount_total'])

                # Split the amount into integer and decimal parts
                integer_part, _, decimal_part = amount_cleaned.partition(',')

                # Convert the integer part to words with French style
                integer_in_words = num2words(int(integer_part), lang='fr').replace('-', ' ').title()

                # If there is a decimal part, convert it separately
                if decimal_part :
                    decimal_in_words = num2words(int(decimal_part), lang='fr').replace('-', ' ').title()
                    record.amount_in_words = integer_in_words #f"{integer_in_words} {decimal_in_words}"
                else:
                    record.amount_in_words = integer_in_words
            else:
                record.amount_in_words = ''  # Handle the case where formatted_amount_total is not present

    amount_in_words = fields.Char(string='Amount in Words', compute='_compute_amount_in_words')
    """
    @api.depends('tax_totals')
    def _compute_amount_in_words(self):
        for record in self:
            if 'formatted_amount_total' in record.tax_totals:
                # Remove currency symbols and commas
                amount_cleaned = re.sub(r'[^\d.]', '', record.tax_totals['formatted_amount_total'].replace('.', ','))

                # Convert the cleaned amount to words
                amount_in_words = num2words(float(amount_cleaned), lang='fr').replace('-', ' ').title()
                record.amount_in_words = amount_in_words
            else:
                record.amount_in_words = ''  # Handle the case where formatted_amount_total is not present

    amount_in_words = fields.Char(string='Amount in Words', compute='_compute_amount_in_words')
    """
