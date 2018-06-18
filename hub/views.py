from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
import random

def tem_igual(seq, v):
    for s in seq:
        if set(v)==set(s):
            return True
    return False

def pagina_inicial_view(request):

    return render (request, "index.html")

def apps_view(request):
    return render(request, "apps.html")

def experimentos_view(request):
    return render(request, "experimentos.html", locals())

def tooltip(request):
    text_content = 'af'
    return render(request, "tooltip.html", locals())

def sequencia_kit(request):
    if request.POST:
        tam = int(request.POST.get("tam",0))
        qtd = int(request.POST.get("qtd",0))
        minimo = int(request.POST.get("min",0))
        maximo = int(request.POST.get("max",0))
        sequencias = []
        for i in range(0,qtd):
            randnums= random.sample(range(minimo, maximo+1), tam)
            if not tem_igual(sequencias,randnums):
                sequencias.append(randnums)
            else:
                i=i-1;
    return render(request, "sequencias.html", locals())
