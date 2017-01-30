from django.conf.urls import include, url
from django.contrib import admin
from principal.views import pagina_inicial_view

urlpatterns = [
    url(r'^', pagina_inicial_view,name="pagina_inicial_view"),
    url(r'^admin/', admin.site.urls),
    url(r'^principal/', include('principal.urls', namespace='principal')),
]
