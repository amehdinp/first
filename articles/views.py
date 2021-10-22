from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def articles_list(request):
    return HttpResponse("articles_list")

def creat_article(request):
    return HttpResponse("creat_article")


def details(request):
    return HttpResponse("details")
