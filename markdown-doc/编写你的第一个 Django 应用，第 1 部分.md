# 编写你的第一个 Django 应用，第 1 部分
(base) XXXX@HaobindeMacBook-Air ~ % python -m django --version<br>
5.1.4

## 创建项目
```
$ mkdir djangotutorial

$ django-admin startproject mysite djangotutorial
这将在目录mysite内创建一个名为的项目djangotutorial 。
```
项目文件解析：<br>
├── djangotutorial<br>
│   ├── manage.py<br>
│   └── mysite<br>
│       ├── __init__.py<br>
│       ├── asgi.py<br>
│       ├── settings.py<br>
│       ├── urls.py<br>
│       └── wsgi.py<br>
这些目录和文件的用处是：[(参考)](https://docs.djangoproject.com/zh-hans/5.1/intro/tutorial01/)

manage.py：一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读django-admin 和 manage.py获取所有manage.py细节。

mysite/：项目的实际 Python 包目录。其名称是导入其中任何内容时需要使用的 Python 包名称（例如mysite.urls）。

mysite/__init__.py：一个空文件，告诉Python这个目录应该被认为是一个Python包。如果你是Python初学者，请阅读官方文档中的更多关于包的知识。

mysite/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看Django 配置了解细节。

mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读URL 调度器文档来获取更多关于 URL 的内容。

mysite/asgi.py：作为您的项目在 ASGI 兼容的 Web 服务器上的入口运行。阅读如何使用 ASGI 来部署了解更多细节。

mysite/wsgi.py：作为您的项目在 WSGI 兼容的 Web 服务器上运行的入口。阅读如何使用 WSGI 进行配置了解更多细节。

## 用于开发简单的服务器
```
$ python manage.py runserver

$...
Django version 5.1.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
## 创建投票应用
在 Django 中，每一个应用程序都是一个 Python 包，并且遵循着相同的约定。Django 自带一个工具，可以帮助生成应用程序的基础目录结构，这样你就可以专心写代码，而不是创建目录了。


在本教程中，我们将在djangotutorial文件夹中创建投票应用程序。
请确定您现在manage.py所在的目录下，然后运行该行命令来创建一个应用程序：
```
$ python manage.py startapp polls
```<br>
polls<br>
├── __init__.py<br>
├── admin.py<br>
├── apps.py<br>
├── migrations<br>
│   └── __init__.py<br>
├── models.py<br>
├── tests.py<br>
└── views.py<br>
2 directories, 7 files<br>
该目录结构包括投票应用的全部内容。

## 编写第一个视图
打开polls/views.py，把下面这些Python代码输入进去。

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
这是在 Django 中通信的视图。要在浏览器中访问它，我们需要将其映射到一个 URL——因此我们需要定义一个 URL 配置，简称为“URLconf”。这些 URL 配置是在每个 URL 中的Django应用程序内部定义的，它们被称为urls.pyPython文件。

要为polls应用定义一个URLconf，创建一个名为**polls/urls.py**的文件，并包含以下内容：

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
接下来是在mysite项目中配置全局URLconf，要包含在polls.urls中定义的URLconf。因此，在中mysite/urls.py添加对django.urls.include的导入，并在urlpatterns列表中插入一个include()，如下图：

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```
该path()函数至少需要两个参数： route和view。该include()函数允许引用其他 URLconf。每当 Django 遇到时include()，它都会截断匹配到该点的 URL 部分，并将剩余的字符串发送到包含的 URLconf 进行进一步处理。

我们设计include()的理念是因为创建可以即插即用。投票应用有它自己的 URLconf( polls/urls.py)，它们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/" ，或者其他任何路径下，该应用都能够正常工作。

## 检验效果
```
$ python manage.py runserver

...
http://127.0.0.1:8000/polls/
...
```







