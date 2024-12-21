'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 11:31:31
FilePath: /whynot-Django/python222_site1/python222_site1/urls.py
Description: 

项目的路由设置，设置网站的具体网址内容；
项目的路由设置，设置网站的具体网址内容；
项目的路由设置，设置网站的具体网址内容；
项目的路由设置，设置网站的具体网址内容；
项目的路由设置，设置网站的具体网址内容；


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

urlpatterns = [
    path('admin/', admin.site.urls),
]
