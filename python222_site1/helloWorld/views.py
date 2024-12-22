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
    return render(request, "http.html")

    # html = "<font color='red'>  我是index2页面 </font>"
    # return HttpResponse(html, status=200)
    
    # return HttpResponseNotFound()
    
    # return JsonResponse({'name':'张三','age':18})
    
    # content_value = {'name':'张三','age':18}    
    # return render(request, "index.html",context=content_value)

    # return redirect("https://www.bilibili.com/",permanent=True)


def blog(request, id):
    if id == 0:
        return redirect('/static/error.html')
    else:
        return HttpResponse('id是' + str(id) + "的博客页面")


def blog3(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day) + '的博客页面')





#下载文件功能实现

file_path = "/Users/hbc/CHANG_THINKING/whynot-Django/python222_site1/file.zip"

def download_file1(request):
    file = open(file_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="file.zip"'
    
    return response



from django.http import StreamingHttpResponse
def download_file2(request):
    file = open(file_path, 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="file.zip"'
    
    
    return response

from django.http import FileResponse
def download_file3(request):
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="file.zip"'
    
    
    return response






def get_test(request):
    """
    get请求测试
    :param request:
    :return:
    """
    print('*'*50)
    print('method:', request.method)  # 请求方式
    # 常用属性
    print('content_type:', request.content_type)
    print('content_params:', request.content_params)
    print('COOKIES:', request.COOKIES)
    print('scheme:', request.scheme)
    # 常用方法
    print('is_secure:', request.is_secure())
    print('host:', request.get_host())
    print('full_path:', request.get_full_path())
    
    
    print('name:', request.GET.get("name"))
    print('pwd:', request.GET.get("pwd"))
    print('aaa:', request.GET.get("aaa", "666"))
    print('*'*50)
    return HttpResponse("http get ok")

def post_test(request):
    """
    post请求测试
    :param request:
    :return:
    """
    print(request.method) # 请求方式
    print(request.POST.get("name"))
    print(request.POST.get("pwd"))
    print(request.POST.get("aaa", "7777"))
    
    return HttpResponse("http post ok")



def to_login(request):
    return render(request, "login.html")