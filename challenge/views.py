from __future__ import unicode_literals, absolute_import

from challenge.forms import SendEmailForm
from challenge.models import Email

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class CreateEmailView(generic.TemplateView):
    template_name = 'challenge/email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FORM'] = SendEmailForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SendEmailForm(request.POST)
        form.send_email()
        return HttpResponseRedirect(reverse('list-email'))


class ListEmailView(generic.ListView):
    template_name = 'challenge/email_list.html'
    model = Email

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pk')
