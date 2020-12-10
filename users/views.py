from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import Users

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.create(username=username, password=password)
        return redirect('/login/')


def login(request):
    return render(request, 'login.html')