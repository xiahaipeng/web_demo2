from django.shortcuts import render
from django.http import HttpResponse

def helloworld_view(request):
    return HttpResponse('<h1>hello world</h1>')