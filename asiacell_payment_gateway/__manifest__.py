# __manifest__.py
{
    'name': 'Asiacell Payment Gateway',
    'version': '17.0',
    'category': 'Accounting',
    'summary': 'Asiacell Payment Gateway Integration for Odoo',
    'description': 'Integrates Asiacell payment gateway into Odoo for seamless payment processing.',
    'author': 'Aioneum',
    'depends': ['account', 'payment'],
    'data': [
        'views/payment_gateway_views.xml',
        'templates/payment_gateway_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
