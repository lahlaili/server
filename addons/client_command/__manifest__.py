# -*- coding: utf-8 -*-
{
    'name': "client_command",

    'summary': """
        Affectation matériel au l'employé""",

    'description': """

    """,

    'category': 'purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'reports/report.xml',
        'views/view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
