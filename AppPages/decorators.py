from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('App'+request.user.groups.capitalize()+':dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper_func

def redirect_dashboard(view_func):
    def wrapper_func(request, *args, **kwargs):
        print('App'+request.user.groups.capitalize()+':dashboard')
        return HttpResponseRedirect(reverse('App'+request.user.groups.capitalize()+':dashboard'))
    return wrapper_func

def redirect_profile(view_func):
    def wrapper_func(request, *args, **kwargs):
        print('App'+request.user.groups.capitalize()+':profile')
        return HttpResponseRedirect(reverse('App'+request.user.groups.capitalize()+':profile'))
    return wrapper_func
