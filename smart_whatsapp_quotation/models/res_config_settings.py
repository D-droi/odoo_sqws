from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_whatsapp_template = fields.Text(
        string='Default WhatsApp Template',
        config_parameter='smart_whatsapp_quotation.default_whatsapp_template',
        default="Merhaba {customer_name}, teklifinizi buradan inceleyebilirsiniz: {pdf_url}",
        help="Use {customer_name} and {pdf_url} as placeholders in your template."
    ) 