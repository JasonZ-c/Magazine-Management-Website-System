from django.http import HttpResponse
from ..models import Task, TaskList
from django.contrib.auth.models import User
from django.http import JsonResponse


def tasklists(request):
    department = request.POST.get('type')
    coco = request.POST.get('co')
    if department == 'cs':
        did = 3
    elif department=='ee':
        did = 2
    elif department=='physics':
        did = 14
    elif department=='chemistry':
        did=4
    #print(did)
    tasks = Task.objects.filter(task_list=did)
    if coco == 'yes':
        tasks = tasks.filter(completed=True).order_by("-created_date")
    else:
        tasks = tasks.filter(completed=False).order_by("-created_date")
    #print(tasks)
    tasks = list(tasks)
    mess = list()
    au = User.objects.all()
    for tk in tasks:
        cb = au.filter(id=tk.created_by_id).first()
        st = au.filter(id=tk.assigned_to_id).first()
        if tk.completed == 1:
            yn = '已完成'
        else:
            yn = '未完成'
        inter = {'date': tk.created_date,
                 'imagesrc': 'http://127.0.0.1:8001'+tk.fmpath,
                 'title': tk.title,
                 'created_by': cb.username,
                 'send_to': st.username,
                 'comp': yn,
                 'bian': tk.id}
        #print(inter)
        mess.append(inter)
    context = {'main': mess}
    return JsonResponse(context)
