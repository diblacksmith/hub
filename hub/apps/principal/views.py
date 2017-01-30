from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect



def pagina_inicial_view(request):

    return render (request, "index.html")

def apps_view(request):

    return render(request, "apps.html")
