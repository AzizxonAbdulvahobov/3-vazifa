from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length = 13)
    body = models.TextField()
    is_checked = models.BooleanField(default = False)
    