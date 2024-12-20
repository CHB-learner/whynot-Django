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
