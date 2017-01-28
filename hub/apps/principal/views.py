from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect



def pagina_inicial(request):

    return render (request, "principal.html")
