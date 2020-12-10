from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def register(request):
    return render(request, 'register.html')