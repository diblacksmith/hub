from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apps_python/$', views.apps_view, name="apps_view"),
    url(r'^experimentos_webdesign/$', views.experimentos_view, name="experimentos_view"),
]
