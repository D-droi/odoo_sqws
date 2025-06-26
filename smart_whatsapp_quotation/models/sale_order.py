from odoo import models, fields, api
from odoo.exceptions import UserError
import re
import urllib.parse


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # WhatsApp related fields
    whatsapp_enabled = fields.Boolean(string='WhatsApp Enabled', default=True)
    whatsapp_phone = fields.Char(string='WhatsApp Phone')
    whatsapp_template = fields.Text(string='WhatsApp Template')
    whatsapp_sent = fields.Boolean(string='WhatsApp Sent', default=False)
    whatsapp_sent_date = fields.Datetime(string='WhatsApp Sent Date')
    whatsapp_status = fields.Selection([
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed')
    ], string='WhatsApp Status', default='pending')
    whatsapp_history_ids = fields.One2many('whatsapp.history', 'sale_order_id', string='WhatsApp History')

    def action_send_whatsapp(self):
        """
        Send quotation via WhatsApp Web
        """
        self.ensure_one()
        
        # Check if partner has mobile or phone number
        partner = self.partner_id
        phone = partner.mobile or partner.phone
        
        if not phone:
            raise UserError("The customer doesn't have a mobile or phone number configured.")
        
        # Generate quotation PDF and get public URL
        try:
            # Dynamically detect the appropriate quotation PDF report
            report_action = self._get_quotation_report_action()
            
            # Generate PDF report
            pdf_content, pdf_type = report_action._render_qweb_pdf([self.id])
            
            # Create attachment for the PDF
            attachment = self.env['ir.attachment'].create({
                'name': f'Quotation_{self.name}.pdf',
                'type': 'binary',
                'datas': pdf_content,
                'res_model': 'sale.order',
                'res_id': self.id,
                'public': True,
            })
            
            # Get the public URL for the PDF
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            pdf_url = f"{base_url}/web/content/{attachment.id}?download=true"
            
        except Exception as e:
            raise UserError(f"Error generating PDF: {str(e)}")
        
        # Format phone number to international format
        formatted_phone = self._format_phone_number(phone)
        
        # Get configurable WhatsApp template from settings
        template = self.env['ir.config_parameter'].sudo().get_param(
            'smart_whatsapp_quotation.default_whatsapp_template',
            "Merhaba {customer_name}, teklifinizi buradan inceleyebilirsiniz: {pdf_url}"
        )
        
        # Format the message using the template
        customer_name = partner.name or 'Customer'
        message = template.format(customer_name=customer_name, pdf_url=pdf_url)
        
        # URL encode the message
        encoded_message = urllib.parse.quote(message)
        
        # Create WhatsApp URL
        whatsapp_url = f"https://wa.me/{formatted_phone}?text={encoded_message}"
        
        # Update WhatsApp status
        self.write({
            'whatsapp_sent': True,
            'whatsapp_sent_date': fields.Datetime.now(),
            'whatsapp_status': 'sent',
        })
        
        # Create WhatsApp history record
        self.env['whatsapp.history'].create({
            'sale_order_id': self.id,
            'send_date': fields.Datetime.now(),
            'status': 'sent',
            'message': message,
            'phone': formatted_phone,
        })
        
        # Return action to open WhatsApp
        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_url,
            'target': 'new'
        }
    
    def _get_quotation_report_action(self):
        """
        Dynamically detect the appropriate quotation PDF report for sale.order
        """
        # Search for custom quotation reports for sale.order
        custom_reports = self.env['ir.actions.report'].search([
            ('model', '=', 'sale.order'),
            ('report_type', '=', 'qweb-pdf'),
            ('report_name', '!=', 'sale.report_saleorder')
        ], order='sequence, id')
        
        # If custom reports exist, use the first one (highest priority)
        if custom_reports:
            return custom_reports[0]
        
        # Otherwise, fall back to the default sale order report
        default_report = self.env.ref('sale.action_report_saleorder', raise_if_not_found=False)
        if not default_report:
            raise UserError("Default sale order report not found.")
        
        return default_report
    
    def _format_phone_number(self, phone):
        """
        Format phone number to international format
        Remove spaces, dashes, and other non-digit characters
        Handle Turkish numbers (starting with 0, replace with 90)
        """
        if not phone:
            return phone
        
        # Remove all non-digit characters
        digits_only = re.sub(r'[^\d]', '', phone)
        
        # Handle Turkish numbers (starting with 0)
        if digits_only.startswith('0'):
            digits_only = '90' + digits_only[1:]
        
        # If it doesn't start with a country code, assume it's a local number
        # You might want to customize this based on your country
        if len(digits_only) == 10 and digits_only.startswith('5'):
            # Turkish mobile number without country code
            digits_only = '90' + digits_only
        
        return digits_only


class WhatsAppHistory(models.Model):
    _name = 'whatsapp.history'
    _description = 'WhatsApp History'
    _order = 'send_date desc'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')
    send_date = fields.Datetime(string='Send Date', required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('delivered', 'Delivered'),
        ('read', 'Read')
    ], string='Status', default='pending')
    message = fields.Text(string='Message')
    response = fields.Text(string='Response')
    phone = fields.Char(string='Phone Number') 