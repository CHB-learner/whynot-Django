'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 11:31:31
FilePath: /whynot-Django/python222_site1/python222_site1/urls.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''

"""
URL configuration for python222_site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

import helloWorld.views
from django.conf import settings
import  os
from django.urls import re_path
from django.views.static import serve
from django.views.generic import RedirectView


from django.urls import include

# import user.views
# import order.views

urlpatterns = [
    # Auth认证
    # 跳转注册页面
    path('auth/toRegister', helloWorld.views.to_register),
    # 提交注册请求
    path('auth/register', helloWorld.views.register),
    # 跳转登录页面
    path('auth/toLogin', helloWorld.views.to_login),
    # 提交登录请求
    path('auth/login', helloWorld.views.login),




    path("admin/", admin.site.urls),
    
    
    path('transfer2/', helloWorld.views.transfer2),
    path('book/preAdd2', helloWorld.views.preAdd2),
    path('book/preAdd3', helloWorld.views.preAdd3),
    
    path('book/preAdd', helloWorld.views.preAdd),
    path('book/add', helloWorld.views.add),
    path('book/delete/<int:id>', helloWorld.views.delete),
    
    path('book/preUpdate/<int:id>', helloWorld.views.preUpdate),
    path('book/update', helloWorld.views.update),
    
    path('book/list', helloWorld.views.bookList),
    path('book/list2', helloWorld.views.bookList2),
    path("time_now/", helloWorld.views.time_now),
    path('toCourse/', helloWorld.views.to_course),
    # path("index/", helloWorld.views.index),
    path('index/', helloWorld.views.index, name="index"),
    path("index2/", helloWorld.views.index2,name="index2"),
    # path('redirectTo',RedirectView.as_view(url='index/')),
    # path("blog/<int:id>", helloWorld.views.blog),
    # re_path('blog3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})',helloWorld.views.blog3),
    # # 配置媒体文件的路由地址
    # re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT},name='media')
    path('user/', include(('user.urls','user'),namespace='user')),
    path('order/', include(('order.urls','order'),namespace='order')),
    path('download1/',helloWorld.views.download_file1),
    path('download2/',helloWorld.views.download_file2),
    path('download3/',helloWorld.views.download_file3),
    path('get/',helloWorld.views.get_test),
    path('post/',helloWorld.views.post_test),
    path('to_login/',helloWorld.views.to_login),
    path('login/',helloWorld.views.login),
    path('to_upload/',helloWorld.views.to_upload),
    path('upload/',helloWorld.views.upload),
    # path('student/list.html',helloWorld.views.List.as_view()),
    path('student/list/', helloWorld.views.List.as_view()),
    path('student/<int:pk>/', helloWorld.views.Detail.as_view()),
    path('student/create/', helloWorld.views.Create.as_view()),
    path('student/update/<int:pk>/', helloWorld.views.Update.as_view()),
    path('student/delete/<int:pk>/', helloWorld.views.Delete.as_view()),
]












