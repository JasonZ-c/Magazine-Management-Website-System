"""ustcserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import login as login_views
from .views import logout as logout_views
from .views import list_count
from .views import task_list
from .views import task_detail
from .views import task_detail_feng
from .views import task_mine
from django.views.static import serve
from django.conf.urls import url
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_views.logined),
    path("logout", logout_views.logouted),
    path("list_count", list_count.list_lists),
    path("task_list", task_list.tasklists),
    path("task_detail", task_detail.taskdetail),
    path("task_detail_feng", task_detail_feng.taskdetailfeng),
    path("task_mine", task_mine.taskmine),
    path("task_add", task_mine.taskadd),
    path("task_sendmail", task_mine.tasksendmail),
    path("task_addcomment", task_detail.taskaddcomment),
    path("task_addfile", task_detail.taskaddfile),
    path("task_pass", task_detail.taskpass),
    #path("comment_show", comment_show.commentshow),
    #path("login", auth_views.LoginView.as_view(), name="login"),
    url(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]
