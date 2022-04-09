from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from niceStore import views

urlpatterns = [
    path('', views.index, name='index'),
]
