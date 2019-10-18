from __future__ import unicode_literals

from challenge.models import Email

from django import forms


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        exclude = ('status',)


class SendEmailForm(forms.Form):
    recipient = forms.CharField(max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Separate emails with comma'}))
    subject = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea())

    def save(self):
        if self.is_valid():
            data = self.cleaned_data
            recipients = self.cleaned_data['recipient'].split(',')
            for recipient in recipients:
                data['recepient'] = recipient
                EmailForm(data).save()
