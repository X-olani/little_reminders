from django.db import models

# Create your models here.

from datetime import date


class SessionItems(models.Model):
    item = models.TextField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.item
