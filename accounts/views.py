from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from notifications.models import DeiviceID
from django.contrib.auth.models import User
import time


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("/")
        else:
            form = AuthenticationForm()

    return render(request, 'loginpage.html', {'form': form})


def signup_view(request):
    users = User.objects.all()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        name = request.POST.get("name")

        username = request.POST.get('username')
        if form.is_valid() and name.strip() != "":
            user = form.save()
            login(request, user)
            print("starting")
            time.sleep(3)
            print("3 seconds done")
            save_name = User.objects.get(id=request.user.id)
            save_name.first_name = name
            save_name.save()

            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signuppage.html', {"form": form})


@login_required(login_url="/login/")
def about_view(request):
    return render(request, 'about.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
# Create your views here.
