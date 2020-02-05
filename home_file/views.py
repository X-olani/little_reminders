from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from session_file.models import SessionItems
from item_database.models import StoredItems
from notifications.models import DeiviceID
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta


@login_required(login_url="/login/")
def home_view(request):

    showItems = StoredItems.objects.all().order_by('expiry_date')
    showItems = (StoredItems.objects.filter(
        user=request.user)).order_by('expiry_date')

    new_showItems = []
    today = date.today()
    # ----------adding iamge to items that  are close to expiry
    for item in showItems:

        splitDate = str(item.expiry_date).split('-')  # the expiry date

        year = int(splitDate[0])
        month = int(splitDate[1])
        day = int(splitDate[2])
        dateBefore = (datetime(year, month, day) -
                      timedelta(days=2)).strftime("%Y.%m.%d")

        dateBefore = datetime.strptime(
            dateBefore, '%Y.%m.%d')
        if today >= dateBefore.date() and today <= item.expiry_date:
            new_showItems.append(
                {"item": item.item, "expiry_date": item.expiry_date, "id": item.id, "time_icon": "/static/timelogo.svg"})
        elif today >= item.expiry_date:
            new_showItems.append(
                {"item": item.item, "expiry_date": item.expiry_date, "id": item.id, "time_icon": "/static/offfood.svg"})
        else:
            new_showItems.append(
                {"item": item.item, "expiry_date": item.expiry_date, "id": item.id, "time_icon": ""})

   # fake_items = [
    #   showItems[i % len(showItems)] for i in range(100)
   # ]

    return render(request, 'home.html', {"req": request, "items": new_showItems, 'num': len(new_showItems)})


@login_required(login_url="/login/")
def delete_item(request):
    if request.method == "POST":
        id = request.POST.get('id')
        deleteID = StoredItems.objects.get(id=id)
        deleteID.delete()
    return redirect("/")


def get_notifyID(request):

    if request.method == "POST":
        notifyID = request.POST['notifyID']
        try:
            DeiviceID.objects.get(notify_device_id=notifyID)

        except DeiviceID.DoesNotExist:
            saveData = DeiviceID(user_id=request.user.id, notify_device_id=notifyID,
                                 user_fkey=request.user)
            saveData.save()

    return redirect("/")

# Create your views here.
