import requests

from challenge.models import Email

from django.conf import settings

from emailsender.celery import app


@app.task(name='send-message')
def send_message(email_id):
    email = Email.objects.get(pk=email_id)
    status = requests.post(
        settings.MAILGUN_URL,
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": "Mailgun Sandbox <{}>".format(
                settings.MAILGUN_DOMAIN_NAME),
            "to": "<{}>".format(email.recepient),
            "subject": "{}".format(email.subject),
            "text": "{}".format(email.text)})
    email.status = Email.SENT if status.status_code == 200 else Email.FAILED
    email.save(update_fields=['status'])
