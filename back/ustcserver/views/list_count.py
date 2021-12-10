from django.http import HttpResponse
from ..models import Task, TaskList
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models.aggregates import Count
from django.core import serializers


def list_lists(request):
    lists = TaskList.objects.all().order_by("group__name", "name")
    list_count = lists.count()
    '''
    task_count1 = (
        Task.objects.filter(completed=0)
        .filter(task_list__group__in=[1])
        .count()
    )
    '''
    '''
    s = (Task.objects.filter(completed=0).values('task_list_id').annotate(shumu=Count('task_list_id')))

    print(s.annotate(shumu=Count('task_list_id')))

    task_count = serializers.serialize("json", Task.objects.filter(completed=0).values('id', 'task_list_id').
                                       annotate(shumu=Count('id')))
    '''
    #task_count = (
        #Task.objects.filter(completed=0).annotate(shumu=Count('task_list_id'))
    #)
    namelist = list()
    shulist = list()
    dlist = list(lists)
    for yuan in dlist:
        namelist.append(yuan.name)
        #print(yuan.name)
        check = (
                Task.objects.filter(completed=0)
                .filter(task_list__group__in=[yuan.group_id])
                .count()
        )
        #print(check)
        shulist.append(check)
    context = {
        "namelist": namelist,
        "shulist": shulist,
        "list_count": list_count
    }
    #print(context)
    #return HttpResponse(json.dumps(context), content_type='application/json')
    return JsonResponse(context)
