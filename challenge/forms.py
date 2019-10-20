from __future__ import unicode_literals

from challenge.models import Email
from challenge.tasks import send_message

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        exclude = ('status',)


class SendEmailForm(forms.Form):
    recipient = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Separate using comma'}))
    subject = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea())

    def send_email(self):
        if self.is_valid():
            data = self.cleaned_data
            recipients = self.cleaned_data['recipient'].split(',')
            for recipient in recipients:
                try:
                    validate_email(recipient)
                except ValidationError:
                    print("{} is an invalid email address".format(recipient))
                data['recepient'] = recipient
                email = EmailForm(data).save()
                send_message.apply_async(kwargs={'email_id': email.pk})
