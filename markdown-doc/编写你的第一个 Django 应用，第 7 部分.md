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



