from django.contrib import admin
from django.urls import path

from django.shortcuts import render

from fantasy import views

def indexPage(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', views.getAllItems),
    path('', indexPage, name='index'),
]
