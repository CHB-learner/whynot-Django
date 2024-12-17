# 编写你的第一个 Django 应用，第 4 部分

本教程从 教程第 3 部分 结束的地方开始。我们将继续网络投票的应用，并将重点放在表单处理和精简我们的代码上。

从哪里获得帮助：

如果你在阅读本教程的过程中有任何疑问，可以前往 FAQ 的 获取帮助 的版块。



## 编写一个简单的表单
让我们更新一下在上一个教程中编写的投票详细页面的模板 ("polls/detail.html") ，让它包含一个 HTML <form> 元素：

```
polls/templates/polls/detail.html

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

简要说明：

上面的模板在 Question 的每个 Choice 前添加一个单选按钮。 每个单选按钮的 value 属性是对应的各个 Choice 的 ID。每个单选按钮的 name 是 "choice" 。这意味着，当有人选择一个单选按钮并提交表单提交时，它将发送一个 POST 数据 choice=# ，其中# 为选择的 Choice 的 ID。这是 HTML 表单的基本概念。

我们将表单的 action 设置为 {% url 'polls:vote' question.id %}，并设置 method="post"。使用 method="post" （而不是 method="get" ）是非常重要的，因为提交这个表单的行为将改变服务器端的数据。当你创建一个改变服务器端数据的表单时，使用 method="post"。这不是 Django 的特定技巧；这是优秀的网站开发技巧。

forloop.counter 指示 for 标签已经循环多少次。

由于我们创建一个 POST 表单（它具有修改数据的作用），所以我们需要小心跨站点请求伪造。 谢天谢地，你不必太过担心，因为 Django 自带了一个非常有用的防御系统。 简而言之，所有针对内部 URL 的 POST 表单都应该使用 {% csrf_token %} 模板标签。

