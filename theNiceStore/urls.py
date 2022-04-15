from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from niceStore import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blurring', views.blurring, name='blurring'),
    path('nofilter', views.nofilter, name='nofilter'),
    path('hsv', views.hsv, name='hsv'),
    path('gray', views.gray, name='gray'),
    path('matrix', views.matrix, name='matrix'),

]
