from django.http import HttpResponse
from ..models import Task, TaskList,Attachment
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.core.mail import send_mail
import time
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .. import settings
import datetime
from django.utils import timezone

def taskmine(request):
    #lists_new = TaskList.objects.all().order_by("group__name", "name")
    xiaoguan = ['stu11']
    uname = request.POST.get('uname')
    auth = User.objects.filter(username=uname).first()
    if auth.is_staff:
        tasks = Task.objects.filter(assigned_to_id=auth.id).order_by("-created_date")
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
                     'imagesrc': 'http://127.0.0.1:8001' + tk.fmpath,
                     'title': tk.title,
                     'created_by': cb.username,
                     'send_to': st.username,
                     'comp': yn,
                     'bian': tk.id}
            mess.append(inter)
        if auth.username in xiaoguan:
            is_ad = 'yes'
            dept = Group.objects.filter(user=auth.id).first()
            group = Group.objects.get(id=dept.id)
            users = group.user_set.all()
            profs = users.filter(is_staff=True)
            name_list = list()
            for us in profs:
                if us.username not in xiaoguan:
                    inte = {'label': us.username}
                    name_list.append(inte)
        else:
            is_ad = 'no'
            name_list = list()
        context = {'main': mess, 'is_admin': is_ad, 'prof_name': name_list}
    else:
        auth = User.objects.filter(username=uname).first()
        tasks = Task.objects.filter(created_by_id=auth.id).order_by("-created_date")
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
            mess.append(inter)
        context = {'main': mess, 'is_admin': 'no'}
    return JsonResponse(context)


def taskadd(request):
    xiaoguan = ['stu11']
    title = request.POST.get('title')
    ty = request.POST.get('type')
    ty1 = request.POST.get('type1')#分区
    if ty1=='分区1':
        sd=14#小管
        temp=14
    elif ty1=='分区2':
        sd = 14
        temp=2
    elif ty1=='分区3':
        sd = 14
        temp=3
    elif ty1=='分区4':
        sd = 14
        temp=4
    print(ty1,'ty1')
    desc = request.POST.get('desc')
    uname = request.POST.get('uname')
    auth = User.objects.filter(username=uname).first()
    small_admin = User.objects.filter(username=xiaoguan[0]).first()
    dept = Group.objects.filter(user=auth.id).first()
    if request.FILES.get("picfile"):

        data = request.FILES.get("picfile")
        st = str(time.time())
        fname, extension = os.path.splitext(data.name)
        print('getpic!!!',fname)
        if extension != '.jpg':
            inter = {
                'information': 'notjpg'
            }
            return JsonResponse(inter)
        spath = default_storage.save('wfm_' + str(title) + '_' + st + '.jpg', ContentFile(data.read()))
        dest = os.path.join(settings.MEDIA_ROOT, spath)
        add_task = Task(title=title, note=desc, priority=999, created_by_id=auth.id, task_list_id=temp,
                        assigned_to_id=sd, score=0, score_admin=0)
        add_task.fmpath = '/media/wfm_' + str(title) + '_' + st + '.jpg'
    else:# use default imag
        add_task = Task(title=title, note=desc, priority=999, created_by_id=auth.id, task_list_id=temp,
                        assigned_to_id=sd, score=0, score_admin=0)
    add_task.save()

    #add attachment
    f = request.FILES.get('content')
    #uname = request.POST.get('people')
    #mid = request.POST.get('mid')
    #au = User.objects.filter(username=uname).first()
    #ta = Task.objects.filter(id=mid).first()
    Attachment.objects.create(task=add_task, added_by=auth, timestamp=datetime.datetime.now(), file=f)
    #arr = Attachment.objects.filter(task_id=mid).order_by("-timestamp").first()

    task_id=add_task
    inter = {
        'imgsrc': 'http://127.0.0.1:8001'+add_task.fmpath,
        'information': 'isjpg',
        'mess': 'add_success'
    }
    return JsonResponse(inter)


def tasksendmail(request):
    typ = request.POST.get('type')
    obj = request.POST.get('obj')
    print(typ,obj)
    prof = User.objects.filter(username=typ).first()
    ta = Task.objects.filter(id=obj).first()
    ta.assigned_to_id = prof.id
    ta.save()
    recip_list = list()
    recip_list.append(prof.email)
    print(recip_list)
    mes = '学院管理员给你发送了一个文件,请注意查收!'
    tal = send_mail(subject='Task提交',
            message=mes,
            # from_email='jasonc98@163.com',  #发送者邮箱
            from_email='malingla@163.com',  #发送者邮箱
            recipient_list=recip_list, # 接收者邮箱可以写多个
            fail_silently=False)
    if tal:
        return JsonResponse({'mess': 'send_success'})
    else:
        return JsonResponse({'mess': 'send_fail'})


