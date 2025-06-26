# Smart WhatsApp Quotation

A comprehensive Odoo module that enables seamless WhatsApp integration for sales quotations.

## Overview

Smart WhatsApp Quotation provides a complete solution for sending sales quotations directly via WhatsApp. The module integrates with Odoo's sales management system and offers configurable message templates, status tracking, and comprehensive history logging.

## Features

### 🚀 Core Functionality
- **WhatsApp Integration**: Send quotations directly via WhatsApp Web
- **Dynamic PDF Generation**: Uses custom or default quotation reports
- **Phone Number Formatting**: Automatic international format conversion
- **Status Tracking**: Monitor WhatsApp sending status and history

### ⚙️ Configuration
- **Configurable Templates**: Company-wide customizable message templates
- **Settings Integration**: Easy configuration through General Settings
- **Multi-Company Support**: Works across all companies in multi-company setups

### 📊 Tracking & History
- **WhatsApp History**: Complete audit trail of all WhatsApp interactions
- **Status Monitoring**: Track sent, failed, and pending messages
- **Response Logging**: Record customer responses and interactions

## Installation

### Prerequisites
- Odoo 14, 16, 17, or 18
- `sale_management` module installed
- Internet connection for WhatsApp Web

### Installation Steps
1. Copy the `smart_whatsapp_quotation` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the module from Apps menu
4. Configure the WhatsApp template in Settings > General Settings

## Configuration

### Setting Up WhatsApp Template
1. Go to **Settings > General Settings**
2. Find the **"Default WhatsApp Template"** field
3. Configure your message using placeholders:
   - `{customer_name}` - Customer's name
   - `{pdf_url}` - Public URL of the quotation PDF

### Example Templates
```
Turkish: "Merhaba {customer_name}, teklifinizi buradan inceleyebilirsiniz: {pdf_url}"
English: "Hello {customer_name}, you can view your quotation here: {pdf_url}"
Custom: "Dear {customer_name}, please find your quotation at: {pdf_url}"
```

## Usage

### Sending Quotations via WhatsApp
1. Open a **Sale Order/Quotation**
2. Ensure the customer has a mobile or phone number
3. Click the **"Send via WhatsApp"** button in the header
4. WhatsApp Web will open with the pre-filled message
5. Review and send the message

### Viewing WhatsApp History
1. Navigate to **Sales > Configuration > WhatsApp History**
2. View all WhatsApp interactions
3. Track message status and responses

## Module Structure

```
smart_whatsapp_quotation/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── sale_order.py
│   └── res_config_settings.py
├── views/
│   ├── sale_order_view.xml
│   ├── whatsapp_history_view.xml
│   └── res_config_settings_view.xml
├── security/
│   └── ir.model.access.csv
└── static/
    └── description/
        ├── icon.png
        ├── screenshot1.png
        ├── screenshot2.png
        └── README.md
```

## Technical Details

### Models
- **SaleOrder**: Extended with WhatsApp functionality
- **WhatsAppHistory**: Tracks all WhatsApp interactions
- **ResConfigSettings**: Configuration management

### Views
- **Sale Order Form**: WhatsApp button and tab
- **WhatsApp History**: Complete interaction history
- **Settings**: Template configuration

### Security
- **Access Rights**: Proper permissions for WhatsApp history
- **Multi-Company**: Company-specific configurations

## Compatibility

- **Odoo Versions**: 14, 16, 17, 18
- **Dependencies**: sale_management
- **Languages**: Multi-language support
- **Companies**: Multi-company compatible

## Support

For support and questions:
- **Email**: support@yourcompany.com
- **Website**: https://www.yourcompany.com
- **Documentation**: See inline code documentation

## License

This module is licensed under LGPL-3.

## Contributing

Contributions are welcome! Please ensure:
- Code follows Odoo development standards
- Tests are included for new features
- Documentation is updated

## Changelog

### Version 14.0.1.0.0
- Initial release
- WhatsApp Web integration
- Configurable message templates
- WhatsApp history tracking
- Multi-company support

## Roadmap

- [ ] WhatsApp Business API integration
- [ ] Automated message scheduling
- [ ] Advanced template editor
- [ ] Bulk quotation sending
- [ ] WhatsApp status webhooks 