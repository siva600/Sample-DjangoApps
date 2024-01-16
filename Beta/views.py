# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("My second App: Beta")


def help(request):
    help_dict = {'help': "HELP from Beta Views"}
    return render(request, 'Beta/help.html', context=help_dict)
