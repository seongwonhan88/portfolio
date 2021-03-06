
import requests

from portfolio.celery import app
from ..settings import MAILGUN_DOMAIN
from django.conf import settings

@app.task
def send_email(target_email, subject, content, to_self=False):
    """
    Check the documentation for detail usages of mailgun API
    https://documentation.mailgun.com/en/latest/user_manual.html#sending-via-api
    """

    data = {
        "from": "Seongwon Han <admin@mail.seongwonhan.com>",
        "to": target_email,
        "subject": subject,
        "html": content
    }

    if to_self:
        data["from"] = "Portfolio Notice <no-reply@mail.seongwonhan.com>"
    response = requests.post(MAILGUN_DOMAIN, auth=("api", settings.MAILGUN_API_KEY), data=data)
    return response.status_code
