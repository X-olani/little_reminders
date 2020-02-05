from django.db import models
from django.contrib.auth.models import User


class DeiviceID(models.Model):
    #user = models.TextField(default=None)
    user_id = models.TextField(default=None)
    #user = models.ForeignKey(user, on_dleet)
    notify_device_id = models.TextField()
    user_fkey = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, related_name="devices")

    def __str__(self):
        return self.notify_device_id
# Create your models here.
