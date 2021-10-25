from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from . import models,forms

# Create your views here.



def articles_list(request):
    articles1 = models.Article.objects.all()
    arg={'articles':articles1}
    return render(request, 'articles/articles_list.html',arg)

def creat_article(request):
    if request.method=='POST':
        form=forms.CreatArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
        return redirect('articles:list')

    else :
        form=forms.CreatArticle()
    return render (request,'articles/creat_article.html',{'form':form})


#    return render(request,'articles/creat_article.html')


def details(request,slug):
    article=models.Article.objects.get (slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})
