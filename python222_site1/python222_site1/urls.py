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
    path("admin/", admin.site.urls),
    path("index/", helloWorld.views.index),
    path("index2/", helloWorld.views.index2),
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
    path('login/',helloWorld.views.to_login),
]











