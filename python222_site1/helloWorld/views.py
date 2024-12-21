'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 12:53:39
FilePath: /whynot-Django/python222_site1/helloWorld/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')
