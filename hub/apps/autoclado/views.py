# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import re, sqlite3

def index(request):
    return render(request, 'autoclado/index.html', locals())

def buscar_sugestoesView(request):
    texto_completo = request.GET.get("texto_completo")
    conn = sqlite3.connect("autonomus.db")
    cursor = conn.cursor()

    split = texto_completo.split()
    palavra_atual = split[-1] if len(split)>0 else ""
    sql = "SELECT palavra FROM palavras WHERE palavra LIKE '%s' ORDER BY ocorrencias DESC LIMIT 5" % (palavra_atual+"%")

    cursor.execute(sql)
    resultado = [x for x in cursor.fetchall()]

    data = {"resultado":resultado}

    conn.commit()
    conn.close()
    return JsonResponse(data)

def reconhecer_palavrasView(request):
    texto_completo = request.GET.get("texto_completo")
    conn = sqlite3.connect("autonomus.db")
    cursor = conn.cursor()

    split = texto_completo.split()
    if len(split)==0:
        return JsonResponse({resultado:""})

    palavras_adicionadas = []
    for palavra in split:
        sql = "SELECT * FROM palavras WHERE palavra = '%s'" % (palavra)
        cursor.execute(sql)
        lista_resultante = cursor.fetchall()
        if len(lista_resultante) == 0:
            sql = "INSERT INTO palavras (palavra, ocorrencias) VALUES (?,?)"
            cursor.execute(sql,(palavra,1))
        else:
            sql = "UPDATE palavras SET ocorrencias = ? WHERE palavra = ?"
            cursor.execute(sql, (lista_resultante[0][2] + 1, lista_resultante[0][1]))
            palavras_adicionadas.append(palavra)




    data = {"palavras_adicionadas":palavras_adicionadas}

    conn.commit()
    conn.close()
    return JsonResponse(data)
