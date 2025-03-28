# models/payment_gateway.py
from odoo import models, fields, api
from odoo.exceptions import UserError
import requests

class PaymentGatewayAsiacell(models.Model):
    _name = 'payment.gateway.asiacell'
    _description = 'Asiacell Payment Gateway'

    name = fields.Char('Payment Method Name', required=True, default='Asiacell Payment')
    api_key = fields.Char('API Key', required=True)
    api_url = fields.Char('API URL', required=True)

    def validate_payment(self, amount, phone_number):
        """ تأكد من إجراء الدفع باستخدام API Asiacell """
        try:
            # إرسال الطلب إلى API Asiacell
            payload = {
                'amount': amount,
                'phone_number': phone_number,
                'api_key': self.api_key,
            }
            response = requests.post(self.api_url, data=payload)
            if response.status_code == 200:
                result = response.json()
                if result.get('status') == 'success':
                    return True
                else:
                    raise UserError("Payment failed: " + result.get('message', 'Unknown error'))
            else:
                raise UserError("Error with payment gateway API")
        except Exception as e:
            raise UserError(f"Error with Asiacell payment: {str(e)}")
        
        return False
