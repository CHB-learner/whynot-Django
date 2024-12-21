'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 12:53:39
FilePath: /whynot-Django/python222_site1/helloWorld/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''

"""
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 12:53:39
FilePath: /whynot-Django/python222_site1/helloWorld/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse


def index(request):
    print('页面请求处理中')
    # print("helloWorld/views.py")
    return render(request, "index.html")



def index2(request):
    # html = "<font color='red'>  我是index2页面 </font>"
    # return HttpResponse(html, status=200)
    
    # return HttpResponseNotFound()
    
    # return JsonResponse({'name':'张三','age':18})
    
    content_value = {'name':'张三','age':18}    
    return render(request, "index.html",context=content_value)



def blog(request, id):
    if id == 0:
        return redirect('/static/error.html')
    else:
        return HttpResponse('id是' + str(id) + "的博客页面")


def blog3(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day) + '的博客页面')