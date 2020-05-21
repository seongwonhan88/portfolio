from django.template.loader import render_to_string

from common_handler.handlers import send_email
from ..settings import EMAIL_ADDRESS, DEFAULT_REPLY_TEMPLATE, DEFAULT_NOTICE_TEMPLATE


def set_default_reply(target_email, fullname):
    subject = 'Hello, thank you for sending me an email'
    data = {'name': fullname}
    html_content = render_to_string(DEFAULT_REPLY_TEMPLATE, data)
    return send_email(target_email, subject, html_content)


def relay_portfolio_message(customer_email, customer_name, customer_message, message_type):
    subject = f'PORTFOLIO: message from {customer_name}'
    data = {
        'customer': {
            'name': customer_name,
            'email': customer_email,
            'message': customer_message,
        },
        'message_type': message_type
    }
    html_content = render_to_string(DEFAULT_NOTICE_TEMPLATE, data)
    return send_email(EMAIL_ADDRESS, subject, html_content, to_self=True)
