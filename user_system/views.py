#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def test_views(request):
    return render(request, 'index.html')