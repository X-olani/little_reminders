from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .models import SessionItems
from item_database.models import StoredItems
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta


@login_required(login_url="/login/")
def add_view(request):

    return render(request, "add_item.html")


@login_required(login_url="/login/")
def add(request):
    itemError = ""
    dateError = ""

    if request.method == "POST":
        itemName = request.POST.get("itemName")
        expiryDate = request.POST.get('expiryDate')

        dateNow = date.today()
        dateArr = expiryDate.split('-')
        present = datetime.now()
        isDateOkay = False

       # dateNowArray = dateNow.split('-')

        # ----------calculate date-------

        # date(year, month, day)
       # date_N_days_ago = datetime(year, month, day) - timedelta(days=2)
       # print(date_N_days_ago.strftime("%Y-%m-%d"))

     # ----------------------------------------------

        if itemName.strip() == "":
            itemError = "Field Empty"
        else:
            itemError = ""

        if expiryDate == "":

            dateError = "Select Date"
        else:
            year = int(dateArr[0])
            month = int(dateArr[1])
            day = int(dateArr[2])
            notification_date = date_N_days_ago = (
                datetime(year, month, day) - timedelta(days=2))
            notification_date = str(notification_date.strftime(
                '%Y-%m-%d'))  # getting the notification date

            if datetime(year, month, day) < present:
                isDateOkay = True
                dateError = "Date entered shows that item is already expired"
            else:
                isDateOkay = True
                dateError = ""

        if itemName.strip() != "" and expiryDate != "" and isDateOkay != False:
            addToDatabase = StoredItems(
                item=itemName.capitalize(), expiry_date=expiryDate, notification_date=notification_date, user=request.user)
            addToDatabase.save()

    return render(request, 'add_item.html', {'itemError': itemError, "dateError": dateError, "reqs": request})

# Create your views here.
