from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.



def articles_list(request):
    articles1 = models.Article.objects.all()
    arg={'articles':articles1}
    return render(request, 'articles/articles_list.html',arg)

def creat_article(request):
    return render(request,'articles/creat_article.html')



def details(request):
    return render(request,'articles/article_detail.html')
