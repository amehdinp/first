from django.urls import path
from . import views

app_name= "articles"
urlpatterns = [
    path('', views.articles_list, name="list"),
    path('creat',views.creat_article,name="creat"),
    path('<slug>',views.details,name="details"),

]
