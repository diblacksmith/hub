from django.conf.urls import include, url
from django.contrib import admin
from principal.views import pagina_inicial

urlpatterns = [
    url(r'^$', pagina_inicial,name="pagina_inicial"),
    url(r'^admin/', admin.site.urls),
    url(r'^principal/', include('principal.urls', namespace='principal')),
]
