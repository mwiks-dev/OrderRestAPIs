import africastalking
from django.conf import settings

def initialize_africastalking():
    africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)
    sms = africastalking.SMS
    return sms

def send_order_confirmation_sms(phone_number, message):
    sms = initialize_africastalking()
    response = sms.send(message, [phone_number])
    return response
