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





def user_info(request, id):
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        res_data = {
            'id': user.id,
            'name': user.username,
            'gender': user.gender,
            'age': user.age
        }
        return JsonResponse(res_data)


from django.views import View

class LoginView(View):
    def get(self, request):
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html', context={'username': username})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remeber = request.POST.get('remeber')
        try:
            user = Users.objects.get(username=username, password=password)
        except Users.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            response = JsonResponse({'message': 'login success'})
            if remeber == 'true':
                response.set_cookie('username', username, max_age=14 * 24 * 3600)
            return response
