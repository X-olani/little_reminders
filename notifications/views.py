import json
from django.shortcuts import render
import requests
from item_database.models import StoredItems
from notifications.models import DeiviceID
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime, timedelta, date


# Create your views here.


def notify(request):
    dates = StoredItems.objects.all().order_by('expiryDate')
    for i in dates:
        print(i.expiryDate)
    present = str(date.today())
    message = ''

    # ----------------------
    twoDaysDate = date_N_days_ago = datetime.now() + timedelta(days=2)
    twoDaysDate = str(twoDaysDate.strftime('%Y-%m-%d'))
    ItemsCloseToExpiry = StoredItems.objects.filter(
        expiryDate__range=[present, twoDaysDate])  # gets all items that all near expiry date
    print(ItemsCloseToExpiry)

    print(ItemsCloseToExpiry.exists())

    return render(request, "send_note.html")


def send_note(request):

    if request.method == "POST":
        message = request.POST.get('message')
        header = {"Content-Type": "application/json; charset=utf-8",
                  "Authorization": "Basic ZWI2OGMwNGUtN2M1OS00M2VkLTkzM2ItZWJlOTBjZmVkYzk4"}
        payload = {"app_id": "c018927c-6a8c-4c5c-89c1-a09aaf5c7a0e",
                   "included_segments": ["All"],
                   "contents": {"en": message}}

        req = requests.post("https://onesignal.com/api/v1/notifications",
                            headers=header, data=json.dumps(payload))
        print(req.status_code, req.reason)
        return redirect("/notify")


def send_note_to_one(request):

    if request.method == "POST":
        userID = DeiviceID.objects.get(user=request.user)
        print(userID.notifyID)

        message = request.POST.get('message')
        header = {"Content-Type": "application/json; charset=utf-8"}

        payload = {"app_id": "c018927c-6a8c-4c5c-89c1-a09aaf5c7a0e",
                   "include_player_ids": [userID.notifyID],
                   "contents": {"en": message}}
        req = requests.post("https://onesignal.com/api/v1/notifications",
                            headers=header, data=json.dumps(payload))

        print(req.status_code, req.reason)
    return redirect("/notify")
