from django.db import models

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

    class Meta:
        ordering = ['pk']
