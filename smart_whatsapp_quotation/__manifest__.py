{
    'name': 'Smart WhatsApp Quotation',
    'version': '14.0.1.0.0',
    'category': 'Sales',
    'summary': 'Send sales quotations via WhatsApp with PDF links and customizable templates',
    'description': """
Smart WhatsApp Quotation integrates WhatsApp into your Odoo Sales workflow.

Key Features:
- One-click "Send via WhatsApp" button on quotations
- Sends public PDF link of the quotation via WhatsApp Web
- Uses customer's phone number from contact card
- Supports international phone numbers (+90, +44, etc.)
- Customizable WhatsApp message template with placeholders
- No third-party API or WhatsApp Business account required
    """,
    'author': 'İyinet A.Ş.',
    'website': 'https://www.iyinet.com.tr',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_view.xml',
        'views/sale_order_view.xml',
        'views/whatsapp_history_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,  # Changed to True for app visibility on App Store
    'license': 'LGPL-3',
    'images': ['static/description/icon.png.png', 'static/description/thumbnail.png', 'static/description/screenshot1.png.png', 'static/description/screenshot2.png.png'],
    'price': 20.0,
    'currency': 'EUR',
    'support': 'info@iyinet.com.tr',
    'maintainer': 'İyinet A.Ş.',
    'contributors': [],
    'external_dependencies': {},
    'assets': {},
}
