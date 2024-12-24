'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 12:53:39
FilePath: /whynot-Django/python222_site1/helloWorld/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from helloWorld.forms import StudentForm
from django.views.generic.edit import DeleteView



# 定义人类
class Person:  
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age


# def index(request):
#     zhangsan = Person('张三',15)
#     # str
#     str = "俺是 模板引擎 字符串"
#     myDict = {"tom": '666', 'cat': '999', 'wzw': '333'}
#     list_data = ['A','B','C']
#     myTuple = ("python", 222, 3.14, False)
    
#     content_value = {'msg':str,'msg2':myDict,'msg3':zhangsan,'msg4':list_data,'msg5':myTuple}
    
#     # 创建一个对象 
#     return render(request, "index.html",context=content_value)

def index(request): #测试filter
    str = "hello"
    date = datetime.datetime.now()
    myDict = {"tom": '666', 'cat': '999', 'wzw': '333'}
    # 创建一个对象 zhangsan
    zhangsan = Person("张三", 21)
    myList = ["java", "python", "c"]
    myTuple = ("python", 222, 3.14, False)
    content_value = {"msg": str, "msg2": myDict, "msg3": zhangsan, "msg4":
    myList, "msg5": myTuple, "date": date}
    return render(request, 'index.html', context=content_value)




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


def login(request):
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    print(user_name, pwd)
    
    if user_name == 'ccc' and pwd  == 'ccc':
        request.session['user_name'] = user_name
        print('session:', request.session['user_name'])
        print('ccc登录成功')
        response = render(request, "main.html")
        response.set_cookie("remember_me", True)
        
        # return render(request, "main.html")
        return response
    else:
        print('登录失败')
        return render(request, "login.html", context = {"error_info":"用户名或密码错误"})


def to_upload(request):
    return render(request, "upload.html")


import  os

upload_path = "/Users/hbc/CHANG_THINKING/whynot-Django/python222_site1/upload"
# 上传文件
def upload(request):        
    file = request.FILES.get("myfile")
    if file:
        print(file.name)
        with open(os.path.join(upload_path,file.name), 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
        return HttpResponse("文件上传成功")
    else:
        return HttpResponse("上传失败")


from django.views.generic import ListView, DetailView   
from helloWorld.models import StudentInfo




class List(ListView):
    # 设置模版文件
    template_name = 'student/list.html'
    
    # 设置模型外的数据
    extra_context = {'title': '学生信息列表'}
    
    # 查询结果集
    queryset = StudentInfo.objects.all()
    
    # 每页展示5条数据
    paginate_by = 5
    
    # 设置上下文对象名称
    context_object_name = 'student_list'
    print('queryset:',queryset)




class Detail(DetailView):
    # 设置模版文件
    template_name = 'student/detail.html'
    
    # 设置模型外的数据
    extra_context = {'title': '学生信息详情'}
    
    # 设置查询模型
    model = StudentInfo
    
    # 查询结果集
    queryset = StudentInfo.objects.all()
    
    # 设置上下文对象名称
    context_object_name = 'student'
    print('queryset:',queryset)


from django.views.generic.edit import UpdateView
class Update(UpdateView):
    # 设置模版文件
    template_name = 'student/update.html'
    
    # 设置模型外的数据
    extra_context = {'title': '学生信息修改'}
    
    # 设置查询模型
    model = StudentInfo
    
    # 查询结果集
    form_class = StudentForm
    
    # 更新完成后跳转的页面
    success_url = '/student/list'




class Create(CreateView):
    # 设置模版文件
    template_name = 'student/create.html'
    
    extra_context = {'title': '学生表单添加'}
    
    form_class = StudentForm
    
    success_url = '/student/list'



class Delete(DeleteView):
    # 设置模版文件
    template_name = 'student/delete.html'
    
    # 设置模型外的数据
    extra_context = {'title': '学生信息删除'}
    
    # 设置查询模型
    model = StudentInfo
    
    # 查询结果集
    queryset = StudentInfo.objects.all()
    
    # 设置上下文对象名称
    context_object_name = 'student'
    print('queryset:',queryset)
    
    # 删除完成后跳转的页面
    success_url = '/student/list'



def to_course(request):
    """
    跳转课程页面
    :param request:
    :return:
    """
    return render(request, 'course.html')


import datetime

def time_now(request):
    """
    获取当前时间
    :param request:
    :return:
    """
    
    now = datetime.datetime.now()
    return render(request, "time_now.html", context={'time':now})


from helloWorld.models import BookInfo
from django.core.paginator import Paginator
def bookList(request):
    """
    图书列表查询
    """
    # 查询所有信息
    # bookList = BookInfo.objects.all()
    # print(bookList)
    
    
    # 分页查询
    bookList = BookInfo.objects.all()
    p = Paginator(bookList,10)
    bookListpage = p.page(1)
    print('总记录数',BookInfo.objects.count())
    
    content_value = {"title": "图书列表", "bookList": bookListpage}
    return render(request, 'book/list.html', context=content_value)


from helloWorld.models import BookTypeInfo
def bookList2(request):
    """
    多表查询 正常查询 和反向查询
    :param request:
    :return:
    """
    # 正向查询
    book: BookInfo = BookInfo.objects.filter(id=2).first()
    print(book.bookType.bookTypeName)
    # 反向查询
    bookType = BookTypeInfo.objects.filter(id=1).first()
    print(bookType.bookinfo_set.first().bookName)
    print(bookType.bookinfo_set.all())
    content_value = {"title": "图书列表"}
    
    return render(request, 'book/list.html',content_value)



def preAdd(request):
    """
    预处理，添加操作
    :param request:
    :return:
    """
    bookTypeList = BookTypeInfo.objects.all()
    print(bookTypeList)
    content_value = {"title": "图书添加", "bookTypeList": bookTypeList}
    return render(request, 'book/add.html', context=content_value)



def add(request):
    """
    图书添加
    :param request:
    :return:
    """
    # print(request.POST.get("bookName"))
    # print(request.POST.get("publishDate"))
    # print(request.POST.get("bookType_id"))
    # print(request.POST.get("price"))
    book = BookInfo()
    book.bookName = request.POST.get("bookName")
    book.publishDate = request.POST.get("publishDate")
    book.bookType_id = request.POST.get("bookType_id")
    book.price = request.POST.get("price")
    book.save()
    # 数据添加后，获取新增数据的主键id
    print(book.id)
    return bookList(request)


def preUpdate(request, id):
    """
    预处理，修改操作
    :param request:
    :return:
    """
    print("id:", id)
    book = BookInfo.objects.get(id=id)
    print(book)
    bookTypeList = BookTypeInfo.objects.all()
    print(bookTypeList)
    content_value = {"title": "图书修改", "bookTypeList": bookTypeList, "book":
    book}
    return render(request, 'book/edit.html', context=content_value)


def update(request):
    """
    图书修改
    :param request:
    :return:
    """
    book = BookInfo()
    book.id = request.POST.get("id")
    book.bookName = request.POST.get("bookName")
    book.publishDate = request.POST.get("publishDate")
    book.bookType_id = request.POST.get("bookType_id")
    book.price = request.POST.get("price")
    book.save()
    
    # return bookList(request)
    return redirect('/book/list')



def delete(request, id):
    """
    图书删除
    :param request:
    :return:
    """
    # 删除所有数据
    # BookInfo.objects.all().delete()
    # 删除指定id数据
    BookInfo.objects.get(id=id).delete()
    # 根据条件删除多条数据
    # BookInfo.objects.filter(price__gte=90).delete()
    return bookList(request)

from helloWorld.models import AccountInfo
from django.db.models import F
from django.db import transaction




# def transfer2(request):
#     """
#     模拟转账
#     :param request:
#     :return:
#     """
#     a1 = AccountInfo.objects.filter(user='张三')
#     a1.update(account=F('account') + 100)
#     a2 = AccountInfo.objects.filter(user='李四')
#     a2.update(account=F('account') - 100)
    
#     return HttpResponse("OK")




@transaction.atomic
def transfer2(request):
    """
    模拟转账
    :param request:
    :return:
    """
    # 开启事务
    sid = transaction.savepoint()
    try:
        a1 = AccountInfo.objects.filter(user='张三')
        a1.update(account=F('account') + 100)
        a2 = AccountInfo.objects.filter(user='李四')
        a2.update(account=F('account') - 100 )
        # 提交事务 （如不设置，当程序执行完成后，会自动提交事务）
        transaction.savepoint_commit(sid)
        return HttpResponse("转账成功")
    except Exception as e:
        print("异常信息：", e)
        # 事务回滚
        transaction.savepoint_rollback(sid)
        return HttpResponse("转账失败")   

from helloWorld.forms import BookInfoForm
def preAdd2(request):
    """
    预处理，添加操作 使用form表单
    :param request:
    :return:
    """
    form = BookInfoForm()
    context_value = {"title": "图书添加", "form": form}
    return render(request, 'book/add2.html', context_value)






