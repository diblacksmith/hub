from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^buscar_sugestoes$', buscar_sugestoesView, name="buscar_sugestoesView"),
    url(r'^reconhecer_palavras$', reconhecer_palavrasView, name="reconhecer_palavrasView"),
]
