from django.http import HttpResponse
from django.contrib.auth import logout


def logouted(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse('logoutsuccess')
