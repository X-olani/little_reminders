"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from home_file.views import home_view, delete_item, get_notifyID
from accounts.views import login_view, signup_view, logout_view, about_view
from session_file.views import add_view, add
from notifications.views import send_note, notify, send_note_to_one
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
app_name = "mineApp"
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r"^add/$", add_view, name="add"),
    url(r"^add_item/$", add),
    url(r"^signup/$", signup_view,  name='signup'),
    url(r"^login/$", login_view, name='login'),
    url(r"^about/$", about_view, name='about'),
    url(r"^logout/$", logout_view, name="logout"),
    url(r"^delete/$", delete_item),
    url(r"^$", home_view, name="home"),
    url(r"^send_notify_id/$", get_notifyID)



]
urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
