from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^identificarPonto$', identificarPonto_view, name="identificarPonto_view"),
]
