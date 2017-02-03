# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return HttpResponse('byunda')
