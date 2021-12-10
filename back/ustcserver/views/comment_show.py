from django.http import HttpResponse
from ..models import Task, TaskList, Comment
from django.contrib.auth.models import User
from django.http import JsonResponse


def commentshow(request):
    department = request.POST.get('dept')
    tid = request.POST.get('mid')
    state = request.POST.get('sta')
    #print(tid)
    #print(state)
    tk = Task.objects.filter(id=tid).first()
    au = User.objects.all()

    cb = au.filter(id=tk.created_by_id).first()
    inter = {
        'imagesrc': 'http://127.0.0.1:8001'+tk.fmpath,
        'title': tk.title,
        'created_by': cb.username,
        'describe': tk.note
    }
    return JsonResponse(inter)
