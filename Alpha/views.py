# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': "Hello from views.py in Alpha app/index.html!"}
    return render(request, 'Alpha/index.html', context=my_dict)


def stories(request):
    story_heading = {'story': "My Stories"}
    return render(request, 'Alpha/stories.html', context=story_heading)

