# 编写你的第一个 Django 应用，第 7 部分
本教程从 教程第 6 部分 结束的地方开始。我们继续修改在线投票应用，这次我们专注于自定义我们在 教程第 2 部分 初见过的 Django 自动生成后台的过程。

## 自定义后台表单
通过 admin.site.register(Question) 注册 Question 模型，Django 能够构建一个默认的表单用于展示。通常来说，你期望能自定义表单的外观和工作方式。你可以在注册模型时将这些设置告诉 Django。

让我们通过重排列表单上的字段来看看它是怎么工作的。用以下内容替换 admin.site.register(Question)：

```
polls/admin.py¶
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

你需要遵循以下流程——创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register() ——在你需要修改模型的后台管理选项时这么做。

以上修改使得 "Publication date" 字段显示在 "Question" 字段之前：



这在只有两个字段时显得没啥卵用，但对于拥有数十个字段的表单来说，为表单选择一个直观的排序方法就显得你的针很细了。

说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集：

```
polls/admin.py¶
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

添加关联的对象¶
好了，现在我们有了投票的后台页。不过，一个 Question 有多个 Choice，但后台页却没有显示多个选项。

好了。

有两个方法可以解决这个问题。第一个就是仿照我们向后台注册 Question 一样注册 Choice ：

```
polls/admin.py¶
from django.contrib import admin

from .models import Choice, Question

# ...
admin.site.register(Choice)
```

现在 "Choices" 在 Django 后台页中是一个可用的选项了。“添加选项”的表单看起来像这样：


在这个表单中，"Question" 字段是一个包含数据库中所有投票的选择框。Django 知道要将 ForeignKey 在后台中以选择框 select 的形式展示。此时，我们只有一个投票。

还请注意“问题”旁边的“添加另一个问题”链接。每个与另一个具有`ForeignKey``关系的对象都可以免费获得此链接。当你点击“添加另一个问题”时，你会看到一个带有“添加问题”表单的弹出窗口。如果你在该窗口中添加问题并点击“保存”，Django会将问题保存到数据库中，并将其动态添加为你正在查看的“添加选项”表单上的选定选项。

不过，这是一种很低效地添加“选项”的方法。更好的办法是在你创建“投票”对象时直接添加好几个选项。让我们实现它。

移除调用 register() 注册 Choice 模型的代码。随后，像这样修改 Question 的注册代码：

```
polls/admin.py¶
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

加载“添加投票”页面来看看它长啥样：

它看起来像这样：有三个关联的选项插槽——由 extra 定义，且每次你返回任意已创建的对象的“修改”页面时，你会见到三个新的插槽。

在三个插槽的末端，你会看到一个“添加新选项”的按钮。如果你单击它，一个新的插槽会被添加。如果你想移除已有的插槽，可以点击插槽右上角的X。以下图片展示了一个已添加的插槽：



不过，仍然有点小问题。它占据了大量的屏幕区域来显示所有关联的 Choice 对象的字段。对于这个问题，Django 提供了一种表格式的单行显示关联对象的方法。要使用它，只需按如下形式修改 ChoiceInline 申明：


```
polls/admin.py¶
class ChoiceInline(admin.TabularInline): ...
```

通过 TabularInline （替代 StackedInline ），关联对象以一种表格式的方式展示，显得更加紧凑：






## 自定义后台更改列表¶
现在投票的后台页看起来很不错，让我们对“更改列表”页面进行一些调整——改成一个能展示系统中所有投票的页面。

以下是它此时的外观：



默认情况下，Django 显示每个对象的 str()。但有时如果我们能显示单个字段会更有帮助。为此，请使用 list_display admin 选项，该选项是要在对象的更改列表页上以列形式显示的字段名称列表：

```
polls/admin.py¶
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date"]
```

另外，让我们把 教程第 2 部分 中的 was_published_recently() 方法也加上


```
polls/admin.py¶
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

你可以点击列标题来对这些行进行排序——除了 was_published_recently 这个列，因为没有实现排序方法。顺便看下这个列的标题 was_published_recently，默认就是方法名（用空格替换下划线），该列的每行都以字符串形式展示出处。

您可以通过在该方法上使用display() 装饰器（扩展在教程 2polls/models.py中创建的文件）来改进这一点，如下所示：

```
polls/models.py¶
from django.contrib import admin


class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```


更多关于可通过装饰器设置的属性的信息，请参见 list_display。

再次编辑文件 polls/admin.py，优化 Question 变更页：过滤器，使用 list_filter。将以下代码添加至 QuestionAdmin：

```
list_filter = ["pub_date"]
```
这样做添加了一个“过滤器”侧边栏，允许人们以 pub_date 字段来过滤列表：

展示的过滤器类型取决你你要过滤的字段的类型。因为 pub_date 是类 DateTimeField，Django 知道要提供哪个过滤器：“任意时间”，“今天”，“过去7天”，“这个月”和“今年”。

这已经弄的很好了。让我们再扩充些功能:

```
search_fields = ["question_text"]
```
在列表的顶部增加一个搜索框。当输入待搜项时，Django 将搜索 question_text 字段。你可以使用任意多的字段——由于后台使用 LIKE 来查询数据，将待搜索的字段数限制为一个不会出问题大小，会便于数据库进行查询操作。

现在是给你的修改列表页增加分页功能的好时机。默认每页显示 100 项。变更页分页, 搜索框, 过滤器, 日期层次结构, 和 列标题排序 均以你期望的方式合作运行。



## 自定义后台界面和风格¶
在每个后台页顶部显示“Django 管理员”显得很滑稽。这只是一串占位文本。

不过，你可以通过 Django 的模板系统来修改。Django 的后台由自己驱动，且它的交互接口采用 Django 自己的模板系统。

## 自定义你的 工程的 模板¶
在您的目录中创建一个templates目录djangotutorial。模板可以位于 Django 可以访问的文件系统上的任何位置。（Django 以您的服务器运行的任何用户身份运行。）但是，将模板保留在项目内是一种很好的惯例。

打开你的设置文件（mysite/settings.py，牢记），在 TEMPLATES 设置中添加 DIRS 选项：

```
mysite/settings.py¶
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
DIRS 是一个包含多个系统目录的文件列表，用于在载入 Django 模板时使用，是一个待搜索路径。

组织模板

就像静态文件一样，我们 可以 把所有的模板文件放在一个大模板目录内，这样它也能工作的很好。但是，属于特定应用的模板文件最好放在应用所属的模板目录（例如 polls/templates），而不是工程的模板目录（templates）。我们会在 创建可复用的应用教程 中讨论 为什么 我们要这样做。

现在在 templates 目录内创建一个名为 admin 的目录，并将默认的 Django 管理界面模板目录中的模板文件 admin/base_site.html 复制到该目录中。默认的 Django 管理界面模板目录位于 Django 源代码中（django/contrib/admin/templates）。

Django 的源文件在哪里？

如果你不知道 Django 源码在你系统的哪个位置，运行以下命令：

```
/ 
$ python -c "import django; print(django.__path__)"
接着，用你网页站点的名字编辑替换文件内的 {{ site_header|default:_('Django administration') }} （包含大括号）。完成后，你应该看到如下代码：

{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></div>
{% if user.is_anonymous %}
  {% include "admin/color_theme_toggle.html" %}
{% endif %}
{% endblock %}
```
我们会用这个方法来教你复写模板。在一个实际工程中，你可能更期望使用 django.contrib.admin.AdminSite.site_header 来进行简单的定制。

这个模板文件包含很多类似 {% block branding %} 和 {{ title }} 的文本。 {% 和 {{ 标签是 Django 模板语言的一部分。当 Django 渲染 admin/base_site.html 时，这个模板语言会被求值，生成最终的网页，就像我们在 教程第 3 部分 所学的一样。

注意，所有的 Django 默认后台模板均可被复写。若要复写模板，像你修改 base_site.html 一样修改其它文件——先将其从默认目录中拷贝到你的自定义目录，再做修改。

自定义你 应用的 模板¶
机智的同学可能会问： DIRS 默认是空的，Django 是怎么找到默认的后台模板的？因为 APP_DIRS 被置为 True，Django 会自动在每个应用包内递归查找 templates/ 子目录（不要忘了 django.contrib.admin 也是一个应用）。

我们的投票应用不是非常复杂，所以无需自定义后台模板。不过，如果它变的更加复杂，需要修改 Django 的标准后台模板功能时，修改 应用 的模板会比 工程 的更加明智。这样，在其它工程包含这个投票应用时，可以确保它总是能找到需要的自定义模板文件。

更多关于 Django 如何查找模板的文档，参见 加载模板文档。

自定义后台主页¶
在类似的说明中，你可能想要自定义 Django 后台索引页的外观。

默认情况下，它展示了所有配置在 INSTALLED_APPS 中，已通过后台应用注册，按拼音排序的应用。你可能想对这个页面的布局做重大的修改。毕竟，索引页是后台的重要页面，它应该便于使用。

需要自定义的模板是 admin/index.html。（像上一节修改 admin/base_site.html 那样修改此文件——从默认目录中拷贝此文件至自定义模板目录）。打开此文件，你将看到它使用了一个叫做 app_list 的模板变量。这个变量包含了每个安装的 Django 应用。你可以用任何你期望的硬编码链接（链接至特定对象的管理页）替代使用这个变量。

当你熟悉了管理员界面后，阅读 本教程的第 8 部分，学习如何使用第三方包。

