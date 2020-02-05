from django.core.management.base import BaseCommand, CommandError
from notifications.models import DeiviceID
from item_database.models import StoredItems
from datetime import datetime, timedelta, date

from django.utils import timezone
import requests
import json


class Command(BaseCommand):
    help = "sends notification to specific user "

    def handle(self, *args, **kwargs):
        present = str(date.today())
        notify_list = StoredItems.objects.filter(
            notification_date__lte=present)

        # Getting unique users
        users = set()
        user_device_id = []
        for notification in notify_list:
            users.add(notification.user)

        print(users)

        # Run through each unique user
        for user in users:

            a = DeiviceID.objects.filter(user_fkey=user.id)
            for i in a:
                user_device_id.append(i.notify_device_id)
        print(user_device_id)

        if len(user_device_id) != 0:
            message = 'Items are about to go off!'
            header = {"Content-Type": "application/json; charset=utf-8"}

            payload = {"app_id": "c018927c-6a8c-4c5c-89c1-a09aaf5c7a0e",
                       "include_player_ids": user_device_id,
                       "contents": {"en": message}}
            req = requests.post("https://onesignal.com/api/v1/notifications",
                                headers=header, data=json.dumps(payload))

            print(req.status_code, req.reason)
        else:
            print("No item close to expiry date")

        # Run through each device for the user
        # for device in user.devices:
        # Do something with device.notify_device_id

        # pass

        # print(notify_list)
        #print(notify_list.values_list('user', flat=True).distinct())
        # for notify in notify_list.values_list('user', flat=True).distinct():
        #     notify_list.filter(pk__in=notify_list.filter(
        #         user=notify))  # values_list('id', flat=True)[1:])
        # print(notify_list)
        print("done")
