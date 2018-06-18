from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', pagina_inicial_view,name="pagina_inicial_view"),
    url(r'^admin/', admin.site.urls),
    #Experimentos webdesign
    url(r'^experimentos_webdesign/$', experimentos_view, name="experimentos_view"),
    url(r'^tooltip/$', tooltip, name="tooltip"),
    url(r'^sequencia_kit/$', sequencia_kit, name="sequencia_kit"),
    #Apps python
    url(r'^apps_python/$', apps_view, name="apps_view"),
    url(r'^apps_python/torre_de_hanoi/', include('torre_de_hanoi.urls', namespace='torre_de_hanoi')),
    url(r'^apps_python/smartZeus/', include('smartZeus.urls', namespace='smartZeus')),
    url(r'^apps_python/autoclado/', include('autoclado.urls', namespace='autoclado'))
]
