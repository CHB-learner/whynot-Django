# 编写你的第一个 Django 应用，第 3 部分
本教程从 教程2 结束的地方开始。我们将继续开发网络投票应用程序，并将着重于创建公共接口——“视图”。
## 概况
Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」。比如，在一个博客应用中，你可能会创建如下几个视图：

 · 博客首页——展示最近的几项内容。

 · 内容“详情”页——详细展示某项内容。

 · 以年为单位的归档页——展示选中的年份里各个月份创建的内容。

 · 以月为单位的归档页——展示选中的月份里各天创建的内容。

 · 以天为单位的归档页——展示选中天里创建的所有内容。

 · 评论处理器——用于响应为一项内容添加评论的操作。

而在我们的投票应用中，我们需要下列几个视图：

 · 问题索引页——展示最近的几个投票问题。

 · 问题详情页——展示某个投票的问题和不带结果的选项列表。

 · 问题结果页——展示某个投票的结果。

 · 投票处理器——用于响应用户为某个问题的特定选项投票的操作。

在 Django 中，网页和其他内容都是从视图派生而来。每一个视图表现为一个 Python 函数（或者说方法，如果是在基于类的视图里的话）。Django 将会根据用户请求的 URL 来选择使用哪个视图（更准确的说，是根据 URL 中域名之后的部分）。

在你上网的过程中，很可能看见过像这样美丽的 URL：ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B。

别担心，Django 里的 URL 样式 要比这优雅的多！

URL 样式是 URL 的一般形式 - 例如：/newsarchive/year/month/。

为了将 URL 和视图关联起来，Django 使用了 'URLconfs' 来配置。URLconf 将 URL 模式映射到视图。

本教程只会介绍 URLconf 的基础内容，你可以看看 [URL调度器](https://docs.djangoproject.com/zh-hans/5.1/topics/http/urls/) 以获取更多内容。

## 编写更多视图

现在让我们向 polls/views.py 里添加更多视图。这些视图有一些不同，因为他们接收参数：

```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
把这些新视图添加进 polls.urls 模块里，只要添加几个 url() 函数调用就行：

```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
在浏览器中查看 "/polls/34/"。它将运行 detail() 函数并显示您在 URL 中提供的任何 ID。也可以尝试 "/polls/34/results/" 和 "/polls/34/vote/"，这些将显示占位的结果和投票页面。

当有人请求你网站的页面，比如说，"/polls/34/"，Django 会加载 mysite.urls Python 模块，因为它被 ROOT_URLCONF 设置指向。它会找到名为 urlpatterns 的变量并按顺序遍历这些模式。在找到匹配项 'polls/' 之后，它会剥离匹配的文本（"polls/"），然后将剩余的文本 -- "34/" -- 发送给 'polls.urls' URL 配置以进行进一步处理。在那里，它会匹配 '<int:question_id>/'，从而调用 detail() 视图，如下所示：

detail(request=<HttpRequest object>, question_id=34)
问题 question_id=34 来自 <int:question_id>。使用尖括号 "获得" 网址部分后发送给视图函数作为一个关键字参数。字符串的 question_id 部分定义了要使用的名字，用来识别相匹配的模式，而 int 部分是一种转换形式，用来确定应该匹配网址路径的什么模式。冒号 (:) 用来分隔转换形式和模式名。

## 写一个真正有用的视图
每个视图必须要做的只有两件事：

1.返回一个包含被请求页面内容的 **HttpResponse** 对象

2.或者抛出一个异常，比如 **Http404** 。

至于你还想干些什么，随便你。

你的视图可以从数据库里读取记录，可以使用一个模板引擎（比如 Django 自带的，或者其他第三方的），可以生成一个 PDF 文件，可以输出一个 XML，创建一个 ZIP 文件，你可以做任何你想做的事，使用任何你想用的 Python 库。

Django 只要求返回的是一个 HttpResponse ，或者抛出一个异常。


因为 Django 自带的数据库 API 很方便，我们曾在 教程第 2 部分 中学过，所以我们试试在视图里使用它。我们在 index() 函数里插入了一些新内容，让它能展示数据库里以发布日期排序的最近 5 个投票问题，以空格分割：

```
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

这里有个问题：页面的设计写死在视图函数的代码里的。如果你想改变页面的样子，你需要编辑 Python 代码。所以让我们使用 Django 的模板系统，只要创建一个视图，就可以将页面的设计从代码中分离出来。

首先，在你的 polls 目录里创建一个 templates 目录。Django 将会在这个目录里查找模板文件。

你项目的 TEMPLATES 配置项描述了 Django 如何载入和渲染模板。默认的设置文件设置了 DjangoTemplates 后端，并将 APP_DIRS 设置成了 True。这一选项将会让 DjangoTemplates 在每个 INSTALLED_APPS 文件夹中寻找 "templates" 子目录。这就是为什么尽管我们没有像在第二部分中那样修改 DIRS 设置，Django 也能正确找到 polls 的模板位置的原因。

在你刚刚创建的 templates 目录里，再创建一个目录 polls，然后在其中新建一个文件 index.html 。换句话说，你的模板文件的路径应该是 polls/templates/polls/index.html 。因为``app_directories`` 模板加载器是通过上述描述的方法运行的，所以 Django 可以引用到 polls/index.html 这一模板了。


```
模板命名空间:
```
虽然我们现在可以将模板文件直接放在 polls/templates 文件夹中（而不是再建立一个 polls 子文件夹），但是这样做不太好。Django 将会选择第一个匹配的模板文件，如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django 没有办法 区分 它们。我们需要帮助 Django 选择正确的模板，最好的方法就是把他们放入各自的 命名空间 中，也就是把这些模板放入一个和 自身 应用重名的子文件夹里。

将下面的代码输入到刚刚创建的模板文件中：

```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Note:

为了让教程看起来不那么长，所有的模板文件都只写出了核心代码。在你自己创建的项目中，你应该使用 完整的 HTML 文档 。


然后，让我们更新一下 polls/views.py 里的 index 视图来使用模板：

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

上述代码的作用是，载入 polls/index.html 模板文件，并且向它传递一个上下文(context)。这个上下文是一个字典，它将模板内的变量映射为 Python 对象。

用你的浏览器访问 "/polls/" ，你将会看见一个无序列表，列出了我们在 教程第 2 部分 中添加的 “What's up” 投票问题，链接指向这个投票的详情页。

## 一个快捷函数： render()
「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」是一个非常常用的操作流程。于是 Django 提供了一个快捷函数，我们用它来重写 index() 视图：

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```
注意，我们不再需要导入loader 和HttpResponse。不过如果你还有其他函数（比如detail，results和vote）需要使用它的话，就需要保留 HttpResponse 的导入。

该render()函数将请求对象作为其第一个参数，将模板名称作为其第二个参数，将字典作为其可选的第三个参数。它返回使用HttpResponse 给定上下文渲染的给定模板的对象。

## 抛出 404 错误

现在，我们来显示处理投票详情视图——它会指定投票的问题标题。下面是这个视图的代码：

```
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

这里有一个新原则。如果指定问题ID所的问题不存在，这个观点就会回复一个Http404异常。

我们稍后再讨论你需要在polls/detail.html 里输入什么，但是如果你想尝试一下上面的代码是否正常工作的话，你可以先把下面的可能输出进去：

```
polls/templates/polls/detail.html¶
{{ question }}
```
这样你就能够测试了。

## 一个快捷函数：get_object_or_404()
尝试用get() 函数获取一个对象，如果不存在就抛出Http404错误也是一个普遍的流程。Django也提供了一个快捷函数，下面是修改后的详情detail()视图代码：

```
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```
该get_object_or_404()函数将 Django 模型作为其第一个参数，并将任意数量的关键字参数传递给get()模型管理器的函数。Http404如果对象不存在，则会引发异常。

```
设计哲学


还有，为什么模型API不直接提交get_object_or_404()发送呢？ObjectDoesNotExistObjectDoesNotExistHttp404

因为这样做会增加模型层和视图层的耦合性。
指导Django设计的最重要的思想之一就是要保证松散耦合。
一些受控的耦合将被包含在 django.shortcuts模块中。
```


也有get_list_or_404()函数，工作原理和get_object_or_404()一样，除了get()函数被换成filter()函数。如果列表为空的话会抛出Http404异常。

## 使用模板系统

回过头去看看我们的detail()视图。它向模板提供了下游变量question。下面是polls/detail.html模板里正式的代码：

```
polls/templates/polls/detail.html¶
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
模板系统统一使用点符号来访问变量的属性。在示例中，首先 Django 尝试对 对象使用字典查找（然后使用 obj.get(str) 操作），如果失败了就尝试属性查找（然后 obj.str操作），结果是成功了。如果这个操作也失败了的话，就要尝试列表查找（不然 obj[int] 操作）。{{ question.question_text }}question

在 循环中发生的函数调用：被解释为Python代码，将返回一个可迭代的对象，该对象可以在 标签内部使用。{% for %}question.choice_set.allquestion.choice_set.all()Choice{% for %}

## 搬模板中的硬编码URL
还记得吗，我们在polls/index.html里面编写投票链接时，链接是硬编码的：

```
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

这种硬编码、强耦合方法的问题，需要在具有大量模板的项目中更改 URL 并保持一致。但是，由于您在polls.urls模块中的path()函数中定义了name参数，您可以通过使用模板标签来消除对 url 配置中定义的特定 URL 路径的依赖：{% url %}

```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
这个标签的工作方式是在polls.urls模块的URL定义中查找具有指定名称的边界。你可以回想一下，具有名称'detail'的URL是在如下语句中定义的：

```
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
```
如果你想改变投票详情视图的URL，比如想改成polls/specifics/12/，你不用在模板里修改任何东西（包括其他模板），只需在polls/urls.py里面稍微修改一下就行：

```
# added the word 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```

## 为 URL 名称添加命名空间

项目教程只有一个应用，polls。在一个真实的Django项目中，可能会有五个，十个，二十个，甚至更多的应用。Django如何分辨重命名的URL呢？举了个例子，polls 应用有detail观点，可能另一个博客应用也有同名的观点。Django 如何知道标签到底对应哪一个应用的 URL 呢？{% url %}

答案是：在根 URLconf 中添加命名空间。在polls/urls.py文件中稍作修改，加上app_name设置命名空间：

```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

现在，编辑polls/index.html文件，来自：

```
polls/templates/polls/index.html¶
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
修改为具有命名命名空间的详细视图：

```
polls/templates/polls/index.html¶
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
当您对您写的视图感到满意后，请阅读教程的第 4 部分了解基础表单处理和通用视图。
