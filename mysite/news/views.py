from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('<h1>Bubu bebe</h1>')

def test(request):
    # print(dir(request))
    return HttpResponse('<h1>Test</h1>')