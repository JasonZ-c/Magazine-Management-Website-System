from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def logined(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        #name = request.POST.get['name']
        pwd = request.POST.get('password')
        user = authenticate(username=name, password=pwd)
        #user = User.objects.filter(username=name, password=pwd).first()
        if user and user.is_active:
            login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
