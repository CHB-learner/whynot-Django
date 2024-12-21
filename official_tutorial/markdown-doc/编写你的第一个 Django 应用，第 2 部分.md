# 编写你的第一个 Django 应用，第 2 部分
我们将设置数据库，创建第一个模型，并快速介绍 Django 自动生成的后台界面。
## 数据库配置
现在，打开mysite/settings.py。这是一个包含 Django 项目设置的 Python 模块。

默认情况下，DATABASES配置使用 SQLite。如果您是数据库新手，或者只是想尝试 Django，这是最简单的选择。SQLite 包含在 Python 中，因此您无需安装任何其他东西来支持您的数据库。但是，在开始您的第一个真正的项目时，您可能希望使用更具可扩展性的数据库（如 PostgreSQL），以避免日后出现数据库切换问题。

如果您希望使用其他数据库，请参阅详细信息以定制并运行您的数据库。

编辑mysite/settings.py文件前，先设置TIME_ZONE为你自己的时区。

另外，关注一下文件头部的INSTALLED_APPS 设置项。这里包括会在你的项目中启用的所有 Django 应用。应用程序可以在多个项目中使用，你也可以备份和发布应用程序，让其他人使用它们。

通常，INSTALLED_APPS 默认包含以下 Django 的自带应用：

django.contrib.admin-- 管理员站点，你很快就能使用它。

django.contrib.auth-- 认证授权系统。

django.contrib.contenttypes-- 内容类型框架。

django.contrib.sessions-- 会话框架。

django.contrib.messages-- 消息框架。

django.contrib.staticfiles-- 管理静态文件的框架。

这些应用项目被默认启用是为了给常规提供方便。

默认开启的某些应用需要至少一个数据表，所以，在使用它们之前需要在数据库中创建一些表。请执行以下命令：<br>

```
python manage.py migrate

(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  
```
生成内容看/mysite/settings.py

## 创建模型
在 Django 里写一个数据库驱动的 Web 应用的第一步是定义模型 - 元数据库结构设计和附加的其他元数据。

在此投票应用中，需要创建两个模型：问题Question和选项Choice。Question模型包括问题描述和发布时间。Choice模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。

这些概念可以通过一个Python类来描述。按照下面的例子来编辑polls/models.py文件：<br>

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
每个模型都表示为django.db.models.Model一类的子类。每个模型有许多类变量，它们都表示模型里的一个数据库字段。

每个字段都是Field类的实例 - 例如，字符字段被表示为CharField，日期时间字段被表示为DateTimeField。这将告诉 Django 字段每个字段要处理的数据类型。

每个Field类实例变量的名称（例如question_text或pub_date）也是字段名，所以最好使用对机器友好的格式。你将在Python代码里使用它们，而数据库将它们作为列名。

你可以使用可选的选项来Field 定义一个人类必备的名称。这个功能在很多 Django 内部组成部分中都被使用了，并且作为文档的一部分。如果某个字段没有提供这个名称，Django 将使用在上面的例子中，我们只 Question.pub_date定义了对人类友好的名称。对于模型内的其他字段，它们的机器友好名称也被作为人类友好名称使用。

定义某些Field 类实例需要参数。例如CharField 需要一个max_length 参数。这个参数的用处不仅仅用于定义数据库结构，也用于验证数据，我们稍后将看到这方面的内容。

Field 也能够接收多个可选参数；在上面的例子中：我们将votes默认default值，设为0。

注意在最后，我们使用ForeignKey定义了一个。这将告诉 Django，每个Choice对象关系都关联到一个 Question 对象。Django 支持所有常用的数据库关系：多对一、多对多和一对一。

## 激活模型
上面的一段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：

为该应用创建数据库架构（生成语句）。CREATE TABLE

创建可以与Question和Choice对象进行交互的 Python 数据库 API。

但首先要把polls应用安装到我们的项目里。


因为在我们的工程中包含这个应用，我们需要在配置类INSTALLED_APPS中添加设置。因为PollsConfig类写在文件polls/apps.py中，所以它的点式路径是'polls.apps.PollsConfig'。在文件mysite/settings.py中子INSTALLED_APPS项添加点式路径后，它看起来像这样：

```
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
现在你的 Django 项目会包含polls 应用。继续运行下面的命令：<br>

```
$ python manage.py makemigrations polls

(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
```
通过运行makemigrations命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分存储为一次迁移。

迁移是 Django 对于模型定义（因为你的数据库结构）的变化的存储形式 - 它们实际上也只是你磁盘上的一些文件。如果你想的话，你可以阅读一下你模型的迁移数据，它被存储在polls/migrations/0001_initial.py别担心，你不需要每次都阅读迁移文件，但它们被设计成人类可执行的形式，这是为了让你手动调整 Django 的修改方式。

Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令 - 这个命令是migrate，我们马上就会接触它 - 但首先，让我们看看迁移命令会执行哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的SQL：

```
$ python manage.py sqlmigrate polls 0001

(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py sqlmigrate polls 0001  
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

敬请期待以下几点：

输出的内容和你使用的数据库有关，上面的输出示例使用的是 PostgreSQL。

数据库的表名是由应用名( polls)和模型名的小写形式(question和 choice)连接而来。（如果需要，你可以自定义此行为。）

主键(ID)会被自动创建。(当然，你也可以自定义。)

默认的，Django 会在外键字段名后追加字符串"_id"。（同样，这也可以自定义。）

外键关系由生成。你不用关心部分，它只是告诉 PostgreSQL，请在事务全部执行完成之后再创建外键关系。FOREIGN KEYDEFERRABLE

它是针对你正在使用的数据库定制的，因此特定于数据库的字段类型，例如“auto_increment”（MySQL）、“bigint PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY”（PostgreSQL）或“整数主键自动增量” `` ( SQLite) 会自动为您处理。字段名称的引用也是如此——例如，使用双引号或单引号。

这个sqlmigrate并没有真正在你的数据库中的执行迁移 - 相反，它把命令输出到屏幕上，让你看看 Django 认为需要执行哪些 SQL 语句。这在你想看看 Django 到底准备做什么，或者命令当你是数据库管理员时，撰写脚本来大规模处理数据库时需要很有用。

如果你感兴趣，你也可以尝试运行；这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。python manage.py check

现在，再次运行migrate命令，在数据库中创建新定义的模型的数据表:

```
(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```
此migrate选中的命令所有还没有执行过的迁移（Django 通过在数据库中创建一个特殊的表django_migrations来跟踪执行过哪些迁移）并在数据库上应用 - 以便将对模型的更改同步到数据库结构上。

迁移是非常强大的功能，它使你在开发过程中持续的改变数据库结构而无需重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据。我们将在后面的教程中详细介绍深入学习这部分内容，现在，你只需要记住，改变模型需要这三步：

```
编辑models.py文件，改变模型。

运行 为模型的改变生成迁移文件。python manage.py makemigrations

运行 来应用数据库迁移。python manage.py migrate
```

数据库迁移被分层生成并应用两个命令是为了让您能够在代码控制系统上提交迁移数据并排序能够在多个应用里使用；这使得开发更加简单，也给其他开发者和生产环境中的使用带来方便。

通过阅读Django 后台文档，您可以获得有关 manage.py工具的更多信息。

## 初试 API
现在让我们进入交互式Python命令行，尝试一下Django为你创建的各种API。通过以下命令打开Python命令行：

```
$ python manage.py shell
```
我们使用这个而不是命令很简单，使用“python”是因为manage.py会设置DJANGO_SETTINGS_MODULE环境变量，这个变量可以让Django根据mysite/settings.py文件来设置Python包的导入路径。

一旦你进入了shell，就可以探索[数据库API](https://docs.djangoproject.com/zh-hans/5.1/topics/db/queries/)

```
(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py shell
Python 3.12.2 | packaged by conda-forge | (main, Feb 16 2024, 20:54:21) [Clang 16.0.6 ]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.29.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from polls.models import Choice, Question

In [2]: Question.objects.all()
Out[2]: <QuerySet []>

In [3]: from django.utils import timezone

In [4]: q = Question(question_text="What's new?", pub_date=timezone.now())

In [5]: q.save()

In [6]: q.id
Out[6]: 1

In [7]: q.question_text
Out[7]: "What's new?"

In [8]: q.pub_date
Out[8]: datetime.datetime(2024, 12, 12, 5, 41, 50, 80271, tzinfo=datetime.timezone.utc)

In [9]: q.question_text = "man~,what'sup?"

In [10]: q.save()

In [11]: Question.objects.all()
Out[11]: <QuerySet [<Question: Question object (1)>]>

In [12]: 
```

等等。<Question: Question object (1)> 对于我们了解这个对象的细节没什么帮助。让我们通过编辑 Question 模型的代码（位于 polls/models.py 中）来修复这个问题。给 Question 和 Choice 增加 __str__() 方法。

```
from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```
给模型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django 自动生成的 admin 里也使用这个方法来表示对象。

让我们再为此模型添加一个自定义方法：

```
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

新加入的 import datetime 和 from django.utils import timezone 分别导入了 Python 的标准 datetime 模块和 Django 中和时区相关的 django.utils.timezone 工具模块。如果你不太熟悉 Python 中的时区处理，看看 时区支持文档 吧。

保存这些更改并再次运行```python manage.py shell``` 以启动新的 Python 交互式 shell：

```
>>> from polls.models import Choice, Question

# 确保我们为 __str__() 方法添加的功能生效。
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django 提供了一个丰富的数据库查找 API，完全由关键字参数驱动。
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# 获取今年发布的问题。
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 请求一个不存在的 ID，会抛出异常。
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# 根据主键查找是最常见的情况，因此 Django 提供了一个快捷方式来进行主键精确查找。
# 以下语句与 Question.objects.get(id=1) 完全等价。
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 确保我们自定义的方法生效。
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# 为问题添加几个选项。create 调用会创建一个新的 Choice 对象，
# 执行 INSERT 语句，将选项添加到可用选项集合中，并返回新创建的 Choice 对象。
# Django 创建了一个集合（定义为 "choice_set"）用于保存 ForeignKey 关系的另一端
# （例如问题的选项），可以通过 API 访问。
>>> q = Question.objects.get(pk=1)

# 显示关联对象集合中的任何选项 -- 目前还没有。
>>> q.choice_set.all()
<QuerySet []>

# 创建三个选项。
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice 对象可以通过 API 访问其关联的 Question 对象。
>>> c.question
<Question: What's up?>

# 反之亦然：Question 对象可以访问 Choice 对象。
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# API 会自动跟踪关系，可以满足您的需要。
# 使用双下划线分隔关系。
# 您可以查找任意深度的关系，没有限制。
# 查找所有问题的选项，这些问题的发布日期在今年（复用之前创建的 'current_year' 变量）。
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# 删除其中一个选项。使用 delete() 方法来完成。
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()

```

[访问关系对象文档](https://docs.djangoproject.com/zh-hans/5.1/ref/models/relations/)

[ 查找字段 文档](https://docs.djangoproject.com/zh-hans/5.1/topics/db/queries/#field-lookups-intro)

[数据库 API](https://docs.djangoproject.com/zh-hans/5.1/topics/db/queries/)

## 介绍 Django 管理页面
设计哲学

为你的员工或客户生成一个用户添加，修改和删除内容的后台是一项缺乏创造性和乏味的工作。因此，Django 全自动地根据模型创建后台界面。

Django 产生于一个公众页面和内容发布者页面完全分离的新闻类站点的开发过程中。站点管理人员使用管理系统来添加新闻、事件和体育时讯等，这些添加的内容被显示在公众页面上。Django 通过为站点管理人员创建统一的内容编辑界面解决了这个问题。

管理界面不是为了网站的访问者，而是为管理者准备的。

创建一个管理员账号<br>
首先，我们得创建一个能登录管理页面的用户。请运行下面的命令：

```
$ python manage.py createsuperuser
```
键入你想要使用的用户名，然后按下回车键：

```
Username: admin
```
然后提示你输入想要使用的邮件地址：

```
Email address: admin@example.com
```
最后一步是输入密码。你会被要求输入两次密码，第二次的目的是为了确认第一次输入的确实是你想要的密码。

```
Password: **********
Password (again): *********
Superuser created successfully.
```

```
Username (leave blank to use 'hbc'): Aleck
Email address: 1945626852@qq.com
CHB.456369
```

## 启动开发服务器
Django 的管理界面默认就是启用的。让我们启动开发服务器，看看它到底是什么样的。

如果开发服务器未启动，用以下命令启动它：

```
$ python manage.py runserver
```
现在，打开浏览器，转到你本地域名的 “/admin/” 目录， -- 比如 http://127.0.0.1:8000/admin/ 。

<br>
<br>
<br>

## 向管理页面中加入投票应用
但是我们的投票应用在哪呢？它没在索引页面里显示。

只需要再做一件事：我们得告诉管理，问题 Question 对象需要一个后台接口。打开 polls/admin.py 文件，把它编辑成下面这样：

```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

```
注意事项：

这个表单是从问题 Question 模型中自动生成的

不同的字段类型（日期时间字段 DateTimeField 、字符字段 CharField）会生成对应的 HTML 输入控件。每个类型的字段都知道它们该如何在管理页面里显示自己。

每个日期时间字段 DateTimeField 都有 JavaScript 写的快捷按钮。日期有转到今天（Today）的快捷按钮和一个弹出式日历界面。时间有设为现在（Now）的快捷按钮和一个列出常用时间的方便的弹出式列表。

页面的底部提供了几个选项：

保存（Save） - 保存改变，然后返回对象列表。

保存并继续编辑（Save and continue editing） - 保存改变，然后重新载入当前对象的修改界面。

保存并新增（Save and add another） - 保存改变，然后添加一个新的空对象并载入修改界面。

删除（Delete） - 显示一个确认删除页面。

如果显示的 “发布日期(Date Published)” 和你在 教程 1 里创建它们的时间不一致，这意味着你可能没有正确的设置 TIME_ZONE 。改变设置，然后重新载入页面看看是否显示了正确的值。

通过点击 “今天(Today)” 和 “现在(Now)” 按钮改变 “发布日期(Date Published)”。然后点击 “保存并继续编辑(Save and add another)”按钮。然后点击右上角的 “历史(History)”按钮。你会看到一个列出了所有通过 Django 管理页面对当前对象进行的改变的页面，其中列出了时间戳和进行修改操作的用户名：
```




