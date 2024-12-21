'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 20:07:49
FilePath: /whynot-Django/python222_site1/user/urls.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.shortcuts import render
from django.urls import path
from django.contrib import admin


import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', user.views.index),
    path('list/', user.views.list),
]
