from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^apps_python/$', apps_view, name="apps_view"),
]
