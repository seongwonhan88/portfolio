from common_handler.handlers.email import send_email
from personal.settings import EMAIL_ADDRESS


def set_default_reply(target_email, fullname):
    subject = 'Hello, thank you for sending me an email'
    message = f"Hi {fullname}, " \
              f"this is an auto generated email letting you know that your email has been successfully sent. " \
              f"Cheers, " \
              f"Seongwon"
    return send_email(target_email, subject, message)

def relay_portfolio_message(customer_email, customer_name, customer_message, message_type):
    subject = f'PORTFOLIO: message from {customer_name}'
    message = f'email from {customer_email}, regarding {message_type}, {customer_message}'
    return send_email(EMAIL_ADDRESS, subject, message)