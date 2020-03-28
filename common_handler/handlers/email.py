import requests

from common_handler.settings import MAILGUN_DOMAIN
from portfolio.settings import MAILGUN_API_KEY


def send_email(target_email, subject, message, to_self=False):
    data = {
        "from": "Seongwon Han <admin@mail.seongwonhan.com>",
        "to": target_email,
        "subject": subject,
        "text": message
    }
    if to_self:
        data["from"] = "Portfolio Notice <no-reply@mail.seongwonhan.com>"
    response = requests.post(MAILGUN_DOMAIN, auth=("api", MAILGUN_API_KEY), data=data)
    return response