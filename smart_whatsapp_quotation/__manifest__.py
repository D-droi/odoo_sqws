{
    'name': 'Smart WhatsApp Quotation',
    'version': '14.0.1.0.0',
    'category': 'Sales',
    'summary': 'Smart WhatsApp integration for sales quotations',
    'description': """
        This module provides smart WhatsApp integration for sales quotations.
        Features:
        - Send quotations via WhatsApp
        - Track quotation status
        - Automated WhatsApp notifications
        - Configurable message templates
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_view.xml',
        'views/sale_order_view.xml',
        'views/whatsapp_history_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'images': [],
    'price': 0.0,
    'currency': 'EUR',
    'support': 'support@yourcompany.com',
    'maintainer': 'Your Company',
    'contributors': [],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'assets': {},
    'uninstall_hook': '',
    'post_init_hook': '',
    'pre_init_hook': '',
} 
