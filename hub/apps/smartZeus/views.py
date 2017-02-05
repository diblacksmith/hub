# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .forms import IdentificarPonto_form

def index(request):
    formulario = IdentificarPonto_form()
    return render(request, 'smartZeus/index.html', locals())

def identificarPonto_view(request):
    corpo_texto = request.GET.get('corpo_texto', None)

    data = {'corpo_texto': corpo_texto}
    print data['corpo_texto']

    return JsonResponse(data)
