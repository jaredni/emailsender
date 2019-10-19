from __future__ import unicode_literals, absolute_import

from challenge.forms import SendEmailForm
from challenge.models import Email

from django.views import generic


class CreateEmailView(generic.TemplateView):
    template_name = 'challenge/email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FORM'] = SendEmailForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SendEmailForm(request.POST)
        form.save()


class ListEmailView(generic.ListView):
    template_name = 'challenge/email_list.html'
    model = Email
