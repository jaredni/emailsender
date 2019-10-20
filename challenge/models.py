from django.db import models

from challenge.tasks import send_message

STATUS_TYPE = (
    (0, 'Sent'),
    (1, 'Failed'),
    (2, 'Pending'),
)


class Email(models.Model):
    recepient = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, default=2)

    SENT = 1
    FAILED = 2
    PENDING = 3

    def status_text(self):
        return STATUS_TYPE[self.status][1]

    class Meta:
        ordering = ['pk']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_message.apply_async(kwargs={'email_id': self.pk})
