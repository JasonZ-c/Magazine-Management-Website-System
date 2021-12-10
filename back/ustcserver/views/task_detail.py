from django.http import HttpResponse
from ..models import Task, TaskList, Comment, Attachment
from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
from django.utils import timezone


def taskdetail(request):
    department = request.POST.get('dept')
    tid = request.POST.get('mid')
    state = request.POST.get('sta')
    uname = request.POST.get('uname')
    print(tid,'11111')
    #print(state)
    arr = Attachment.objects.filter(task_id=tid).order_by("-timestamp").first()
    #print(arr.filename)
    #print(arr.filename)
    tk = Task.objects.filter(id=tid).first()
    au = User.objects.all()

    cb = au.filter(id=tk.created_by_id).first()

    comments = Comment.objects.filter(task=tid).order_by("-date")
    comments_list = list(comments)
    comm = list()
    for com in comments_list:
        comment_person = au.filter(id=com.author_id).first()
        tabledata = {
            'date': com.date,
            'name': comment_person.username,
            'address': com.body
        }
        comm.append(tabledata)
    if uname == 'fuck!':
        staff = 'fk'
    else:
        at = au.filter(username=uname).first()
        if at.is_staff:
            staff = 'yes'
        else:
            staff = 'no'
    if arr is not None:
        inter = {
            'imagesrc': 'http://127.0.0.1:8001'+tk.fmpath,
            'title': tk.title,
            'created_by': cb.username,
            'describe': tk.note,
            'comments': comm,
            'attachment': 'http://127.0.0.1:8001'+arr.file.url,
            'attachment_name': arr.file.name,
            'is_prof': staff,
            'has_att': 'yes'
        }
    else:
        inter = {
            'imagesrc': 'http://127.0.0.1:8001'+tk.fmpath,
            'title': tk.title,
            'created_by': cb.username,
            'describe': tk.note,
            'comments': comm,
            'has_att': 'no',
            'is_prof': staff
        }
    return JsonResponse(inter)


def taskaddcomment(request):
    uname = request.POST.get('people')
    tid = request.POST.get('mid')
    comm = request.POST.get('content')
    au = User.objects.all()
    ss = au.filter(username=uname).first()
    comment = Comment(body=comm, author_id=ss.id, task_id=tid)
    comment.save()
    return JsonResponse({'mess': '添加评论成功'})


def taskaddfile(request):
    f = request.FILES.get('content')
    uname = request.POST.get('people')
    mid = request.POST.get('mid')
    au = User.objects.filter(username=uname).first()
    ta = Task.objects.filter(id=mid).first()
    Attachment.objects.create(task=ta, added_by=au, timestamp=datetime.datetime.now(), file=f)
    arr = Attachment.objects.filter(task_id=mid).order_by("-timestamp").first()
    #print(arr,'11221',f,'debug',mid)

    inter = {
        'mess': '添加附件成功',
        'attachment': 'http://127.0.0.1:8001' + arr.file.url,
        'attachment_name': arr.file.name
    }
    return JsonResponse(inter)

def taskpass(request):
    mid = request.POST.get('mid')
    ta = Task.objects.filter(id=mid).first()
    ta.completed = 1
    ta.completed_date = timezone.now
    ta.save()
    return JsonResponse({'mess': '该文章已被您通过'})
