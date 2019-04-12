# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Charlie.forms import UserForm, UserProfileInfoForm
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'Charlie/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        # grab the information of both the forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # check if the information is valid
        if user_form.is_valid() and profile_form.is_valid():

            # if valid grab the info from base user form.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # check if there is picture in the form
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        # if there is no post request set the userform and profileform
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'Charlie/registration.html',
                  {'user_from': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

