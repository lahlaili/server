# crm_custom/__manifest__.py

{
    'name': 'CRM Customizations',
    'version': '1.0',
    'summary': 'Customizations for the CRM module',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'category': 'Customer Relationship Management',
    'depends': ['crm'],
    'data': [
        'views/view.xml',
        'views/visite.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
