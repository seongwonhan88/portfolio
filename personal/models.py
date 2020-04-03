from django.db import models

from personal.settings import CHOICES


class ContactInfo(models.Model):
    name = models.CharField('Name', max_length=150, blank=False, null=False)
    email = models.EmailField('Email address', blank=False, null=False)
    message_type = models.CharField('What is this regarding?', max_length=128, choices=CHOICES, blank=False, null=False)
    message_content = models.TextField('Message details', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
