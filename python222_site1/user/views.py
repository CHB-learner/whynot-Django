'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 20:01:48
FilePath: /whynot-Django/python222_site1/user/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.shortcuts import render

# Create your views here.





from django.shortcuts import render
from django.urls import path
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("用户信息--Hello, world. You're at the user index.")


def list(request):
    return HttpResponse("用户列表")