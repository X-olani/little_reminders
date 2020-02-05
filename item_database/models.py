from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StoredItems(models.Model):

    item = models.TextField()
    expiry_date = models.DateField()
    notification_date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stored_items",
    )

    def __str__(self):
        return f"StoredItem<{self.user} {self.item} {self.expiry_date} {self.notification_date}>"

    def __repr__(self):
        return str(self)

#

# user.stored_items
#StoredItems.objects.filter(notification_date__lte = today)
