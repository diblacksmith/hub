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
    sql = """
    SELECT
        (SELECT palavra FROM palavras WHERE id = secundaria_id),
        COUNT(secundaria_id) as num FROM cadeia_palavras
    WHERE primaria_id = (SELECT id FROM palavras WHERE palavra LIKE '%s')
    GROUP BY secundaria_id
    ORDER BY num DESC
    LIMIT 3
    """ % (palavra_atual+"%")
    cursor.execute(sql)
    resultado = [x for x in cursor.fetchall()]
    sql = "SELECT palavra FROM palavras WHERE palavra LIKE '%s' ORDER BY ocorrencias DESC LIMIT 3" % (palavra_atual+"%")

    cursor.execute(sql)
    for r in cursor.fetchall():
        resultado.append(r)

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
        fetchall = cursor.fetchall()
        if len(fetchall) == 0:
            sql = "INSERT INTO palavras (palavra, ocorrencias) VALUES (?,?)"
            cursor.execute(sql,(palavra,1))
        else:
            sql = "UPDATE palavras SET ocorrencias = ? WHERE palavra = ?"
            cursor.execute(sql, (fetchall[0][2] + 1, fetchall[0][1]))
            palavras_adicionadas.append(palavra)

    for i, palavra in enumerate(split):
        if i != 0:
            palavra_anterior = split[i-1]
            cursor.execute("SELECT id FROM palavras WHERE palavra = '%s'" % palavra_anterior)
            primaria_id = cursor.fetchall()[0][0]
        else:
            primaria_id = None

        cursor.execute("SELECT id FROM palavras WHERE palavra = '%s'" % palavra)
        secundaria_id = cursor.fetchall()[0][0]

        sql = "INSERT INTO cadeia_palavras (primaria_id, secundaria_id) VALUES (?,?)"
        cursor.execute(sql,(primaria_id,secundaria_id))
        print i,' inserindo ',primaria_id,secundaria_id

    data = {"mensagem":'palavras e cadeias registradas'}

    conn.commit()
    conn.close()
    return JsonResponse(data)
