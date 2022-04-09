from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from collections import OrderedDict


def index(request):
    return render(request, 'index.html')
