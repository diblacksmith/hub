# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .forms import IdentificarPonto_form
import re

def index(request):
    formulario = IdentificarPonto_form()
    return render(request, 'smartZeus/index.html', locals())

def identificarPonto_view(request):
    hora = re.compile('\d{1,2}[:h]{1}\d*')
    data = re.compile(u'ontem|hoje|segunda|ter[çc]a|quarta|quinta|sexta|s[aá]bado|domingo|\d{1,2}/\d{1,2}/\d*|\d{1,2}/\d{1,2}')
    user_email = re.compile('[a-zA-Z0-9_.]+@(?:lais.huol.ufrn.br|gmail.com)')

    corpo_texto = request.GET.get('corpo_texto', None)

    data = {'horas':hora.findall(corpo_texto), 'datas':data.findall(corpo_texto), 'user_email': user_email.findall(corpo_texto)}
    return JsonResponse(data)
