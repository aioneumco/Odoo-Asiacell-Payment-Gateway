# controllers/main.py
from odoo import http
from odoo.http import request

class AsiacellPaymentController(http.Controller):

    @http.route(['/payment/asiacell'], type='http', auth="public", methods=['POST'], website=True)
    def payment_asiacell(self, **post):
        """استقبال الدفع عبر Asiacell"""
        amount = post.get('amount')
        phone_number = post.get('phone_number')
        gateway = request.env['payment.gateway.asiacell'].search([], limit=1)
        
        if gateway:
            payment_valid = gateway.validate_payment(amount, phone_number)
            if payment_valid:
                return request.redirect('/payment/success')
            else:
                return request.redirect('/payment/failure')
        return request.redirect('/payment/failure')
