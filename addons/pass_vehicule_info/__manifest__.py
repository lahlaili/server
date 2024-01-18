# -*- coding: utf-8 -*-
{
    'name': "gestion parc automobile",

    'summary': """
        Purchase order lines""",

    'description': """
       Introduce a vehicle field within Purchase order lines and ensure its inclusion in receipt and invoice lines.
    """,


    'category': 'purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','fleet', 'account','purchase','sale','sale_stock','product'],

    # always loaded
    'data': [
        'views/product_category_view.xml',
        'views/views_form.xml',
        'views/personnalisation_bon_achat.xml',
        'views/bon_achat_sans_adresse d_expedition.xml',
        'views/personnalisation_facture.xml',
        'views/bon_achat_gasoil.xml',
        'views/product_print.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
