from django.conf.urls import include, url
from . import views

urlpatterns = [
    #Experimentos webdesign
    url(r'^experimentos_webdesign/$', views.experimentos_view, name="experimentos_view"),
    #Apps python
    url(r'^apps_python/$', views.apps_view, name="apps_view"),
    url(r'^apps_python/torre_de_hanoi/', include('torre_de_hanoi.urls', namespace='torre_de_hanoi'))
]
