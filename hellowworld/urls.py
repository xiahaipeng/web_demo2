from django.urls import re_path
from hellowworld import views

urlpatterns = [
    re_path(r'^hello-world/$', views.helloworld_view)
]