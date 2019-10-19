from __future__ import unicode_literals

import json

from challenge.models import Email

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse


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
                    data['recepient'] = recipient
                    EmailForm(data).save()
                except ValidationError:
                    print("{} is an invalid email address".format(recipient))
