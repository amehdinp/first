from django.contrib import admin
from django.urls import path,include
from articles.views import articles_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/' , include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('', articles_list),
]
