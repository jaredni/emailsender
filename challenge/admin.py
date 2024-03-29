from django.contrib import admin

from challenge.models import Email


class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ('recepient', 'subject', 'status')


admin.site.site_url = "/admin/list_email"
admin.site.register(Email, EmailAdmin)
