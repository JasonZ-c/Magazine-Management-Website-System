from django.http import JsonResponse
import os
from .. import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from ..models import Task, TaskList
import time


def taskdetailfeng(request):
    task_id = request.POST.get('mid')
    cont = request.POST.get('content')
    task = Task.objects.filter(id=task_id).first()

    #print(task_id)
    if request.FILES.get("picfile"):
        data = request.FILES.get("picfile")
        st = str(time.time())
        fname, extension = os.path.splitext(data.name)
        #print(extension)
        # pa = os.path.join('fengmian', 'wfm-'+str(task_id)+'.jpg')
        if extension != '.jpg':
            inter = {
                'information': 'notjpg'
            }
            return JsonResponse(inter)
        #yp = os.path.join(settings.MEDIA_ROOT, 'wfm_' + str(task_id) + '_' + st + '.jpg')
        #if os.path.exists(yp):
            #os.remove(yp)
        spath = default_storage.save('wfm_' + str(task_id) + '_' + st + '.jpg', ContentFile(data.read()))
        dest = os.path.join(settings.MEDIA_ROOT, spath)
        task.fmpath = '/media/wfm_' + str(task_id) + '_' + st + '.jpg'
        task.note = cont
        task.save()
    inter = {
        'imgsrc': 'http://127.0.0.1:8001'+task.fmpath,
        'information': 'isjpg'
    }
    return JsonResponse(inter)
