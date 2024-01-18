# -*- coding: utf-8 -*-
{
    'name': "Identifiants fiscaux marocains",

    'summary': """
        identifiants fiscaux marocains""",

    'description': """
       
    """,


    'category': 'purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','web'],

    # always loaded
    'data': [

        'views/res_partner_view.xml',
        'views/custom_footer.xml',
        'views/facture_giac.xml',


    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
