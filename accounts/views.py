from django.shortcuts import render
from django.http import HttpResponse

def singup(request):
    return HttpResponse("signupppp")

def singin(request):
    return HttpResponse("sigin")

def singout(request):
    return HttpResponse("signout")
