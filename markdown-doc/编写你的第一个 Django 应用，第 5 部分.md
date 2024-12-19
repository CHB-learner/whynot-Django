# 编写你的第一个 Django 应用，第 5 部分
本教程从 教程第 4 部分 结束的地方开始。我们已经建立了一个网络投票应用程序，现在我们将为它创建一些自动化测试。

# 自动化测试简介¶
## 自动化什么是测试？¶
测试代码，是为了检查你的代码是否能够正常运行的程序。

测试在不同的层次中都存在。有些测试只关注某些细微的细节（某个模型的某些方法的返回值是否满足预期？），而另一些测试可能检查某个软件的一系列操作（用户输入序列是否造成了预期的结果？）。其实这和我们在教程第2部分，里做的并没有什么不同，我们使用shell来测试上述方法的功能，或者运行某个应用并输入数据来检查它的行为。

真正不同的地方，自动化测试是由修改某个系统帮你自动完成的。当你创建好一系列测试后，每次修改应用代码后，就可以自动检查出后面的代码是否还像你曾经那样这样就可以正常工作了。您不需要花费大量时间来进行手动测试。

## 为什么你需要写测试¶
但是，为什么需要测试呢？又为什么是现在呢？

你可能会觉得学Python/Django对你来说已经很满意了，再学一些新东西的话看起来有点负担过重并且没有必要。毕竟，我们的投票应用看起来已经完美工作了。写自动测试并不能让工作变得更好。如果写一个投票应用是你想用 Django 完成的唯一工作，那你确实没必要学写测试。但是如果你还想写更复杂的项目，现在就是学习测试写法的最重要好时机了。

## 测试节省你的时间¶
在某种程度上，能够「判断出是否正常工作」的测试，就称得上是一个足够的了。在比较复杂的应用程序中，组件之间可能存在着一个复杂的交互。

对其中所有组件的改变，也有可能会造成意想不到的结果。判断「代码是否正常工作」意味着你需要用大量的数据来修改完整的测试全部代码的功能，以确保你的小对应用整体造成破坏——这太费时间了。

尤其是当你发现自动化测试可以在几个自助之内帮助完成这件事时，就会更觉得手动测试实在是太浪费时间了。当有人写出错误的代码时，自动化测试还能帮忙您找到了错误代码的位置。

有时你会觉得，和富有创造和生产力的业务代码比起来，编写枯燥的测试代码实在太无聊了，特别是当你知道你的代码完全没有问题的时候。

然而，编写测试还是花费几个小时手动测试你的应用程序，或者为了找到某个小错误而胡乱翻看代码要有意义的多。

## 不仅能测试发现错误，还能预防错误¶
「测试是开发的对立面」，这种思想是错误的。

如果不进行测试，整个应用的行为就会变得更加不清晰。甚至当你在看自己写的代码时也是这样，有时候你需要仔细研读一段代码才能搞清楚它有什么用。

测试就好像是从内部仔细检查你的代码，当有些地方出错时，这些地方就会变得很明显——即使你自己没有意识到那里写错了。

## 测试使你的代码更强大¶
也许你遇到过这种情况：你编写了一个绝赞的软件，但是其他开发者看都不看一眼，因为它缺乏测试。没有测试的代码不值得信任。 Django 最初开发者的 Jacob 之一Kaplan-Moss 表示：“项目规划时没有包含测试是不科学的。”

其他的开发者希望在正式使用你的代码之前通过测试看到它，这是你需要编写测试的另一个重要原因。

## 测试为什么要协作¶
前面的几点都是从单人开发的角度来说的。复杂的应用可能由团队维护。测试的存在保证了协作者不会不小心破坏了你的代码（也保证你不会不小心弄坏了）坏他们的）。如果你想成为一名 Django 程序员谋生的话，你必须熟练编写测试！

## 基础测试策略¶
有好几种不同的方法可以写测试。

一些程序员遵循一种称为“测试驱动开发”的原则；他们实际上在编写代码之前编写测试。这似乎违反直觉，但实际上它与大多数人经常做的事情类似：他们描述一个问题，然后创建一些代码来解决它。测试驱动开发在 Python 测试用例中将问题形式化。

比较普遍的情况是，一个刚接触自动化测试的新手更倾向于先写代码，然后再写测试。虽然提前写测试可能会更好，但是晚点写起码也比没有强。

有时候很难决定从哪里开始下手写测试。如果你才写了几千行Python代码，选择从哪里开始写测试确实不怎么简单。如果是这种情况，那么在你修改下一步代码（比如加）新功能，或者修复Bug）之前写个测试是比较合理且有效的。

所以，我们现在就开始写吧。

# 开始写我们的第一个测试

幸运的是，我们的polls应用现在存在一个小 bug 需要被修复：我们的要求是如果问题是在一天之内发布的，Question.was_published_recently()方法将会返回True，但是现在这个方法在Question的pub_date字段比当前时间还晚时也返回True（这是一个Bug）。

使用shell确认命令查看该方法的日期错误

```
$ python manage.py shell
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```
因为将来发生的肯定不是最近发生的，所以代码显然是错误的。



## 创建一个测试来引入这个错误¶
我们刚刚在shell里面做自动化测试应该做的工作。所以我们来把它改写成自动化的吧。

一般来说，Django应用的测试应该写在应用的tests.py文件里。测试系统会自动的在所有文件里寻找并执行以test底层的测试函数。

将下面的代码写入polls应用里的tests.py文件内：

```
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```
我们创建了一个django.test.TestCase子类，并添加了一个方法，这个方法创建了一个pub_date未来某天的Question实例。然后检查它的was_published_recently()方法的返回值——它应该是False。


## 运行测试¶
在终端中，我们通过输入以下代码运行测试：

```
$ python manage.py test polls

(base) hbc@HaobindeMacBook-Air djangotutorial % python manage.py test polls
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests.test_was_published_recently_with_future_question)
was_published_recently() returns False for questions whose pub_date
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/hbc/CHANG_THINKING/whynot-Django/djangotutorial/polls/tests.py", line 17, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
以下是自动化测试的运行流程：

python manage.py test polls 将寻找 polls应用里的测试代码

它找到了django.test.TestCase一个子类

它创建了一个特殊的数据库供测试使用

它在类中寻找测试方法——以test开头的方法。

在 test_was_published_recently_with_future_question方法中，它创建了一个pub_date值为 30 天后的Question实例。

使用assertls()方法，发现was_published_recently()返回了True，而我们期望它返回False。

测试系统通知我们哪些测试样例失败了，并造成测试失败的代码所在的行号。
## 修复此错误

我们无数次知道，当pub_date为未来的某天时，Question.was_published_recently()应该返回False。我们修改models.py里的方法，只在日期是过去式的时候才返回True：

```
polls/models.py¶
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```
然后再次运行：

```
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Destroying test database for alias 'default'...
```
发现bug后，我们编写了能够暴露这个bug的自动化测试。在修复bug之后，我们的代码顺利的通过了测试。

将来，我们的应用程序可能会出现其他的问题，但是我们可以肯定的是，一定不会再次出现这个bug，因为只要运行反复测试，就会立刻收到警告。我们可以认为应用程序的这一小部分代码永远是安全的。

## 更全面的测试
我们已经搞定了一部分了，现在可以全面考虑的测试was_published_recently()这个方法修复它的安全性，然后就可以把这个方法稳定下来了。事实上，在修复一个bug的时候不小心引入另一个bug会是非常好的令人尴尬的。

我们在上次写的类里再增加两个测试，来更全面的测试这个方法：

```
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

现在，我们有三个测试来确保Question.was_published_recently()过去、最近和未来的透明情况都返回正确的值。

再次申明， polls 现在是一个小型的应用程序，但是无论它以后变得多么复杂，无论他和其他代码如何交互，我们都可以在一定的编程中保证我们所编写的测试的方法将按照预期的方式运行。
# 测试视图¶
我们对所有问题的投票应用都一视同仁：它不会发布所有的问题，也包括那些pub_date字段值是未来的问题。我们应该改进这一点。如果pub_date设置为未来的某天，这应该被解释为这个问题将在所填写的时间点才被发布，而在之前是不可见的。

## 针对审查的测试¶
为了修复上述 bug，我们这次先编写测试，然后再去修改代码。事实上，这是一个「测试驱动」开发模式的实例，但其实这两者的顺序不太重要。

在我们的第一个测试中，我们关注代码的内部行为。我们通过用户使用模拟浏览器访问被测试的应用程序来检查代码行为是否符合预期。

在我们动手之前，先看看需要用到的工具。

## Django 测试工具之客户端

Django 提供了一个供测试使用的Client来模拟用户和视图层代码的交互。我们tests.py甚至 可以在shell中使用它。

我们从 shell开始开始，首先我们做一些在tests.py不是必须的准备工作。第一步是在中 shell配置测试环境：

```
/ 
$ python manage.py shell
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

setup_test_environment()安装了一个模板渲染器，这需要我们能够检查响应上的一些额外属性，例如response.context，否则将无法使用此功能。请注意，这个方法不会建立一个测试数据库，所以下面的内容将针对现有的数据库运行，输出结果可能会不同，这取决于您已经创建了哪些问题。如果您中settings.py的TIME_ZONE不正确，您可能会得到意外的结果。如果您不记得之前的配置，请在继续之前检查。

接下来，我们需要导入测试客户端类（前面在tests.py中，我们将使用django.test.TestCase类，它自带一个客户端，所以这个步骤不是必需的）：

```
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
准备好后，我们可以要求客户端为我们执行一些工作：

>>> # get a response from '/'
>>> response = client.get("/")
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

# 改进审查代码
现在的投票列表将显示未来的投票（pub_date值为未来的某天）。我们来修复这个问题。

在教程的第 4 部分 里，我们介绍了基于ListView的视图类：

```
polls/views.py

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

```	
我们需要改进 get_queryset()方法，让他能够通过将 Question 的 pub_data 属性与timezone.now()比较来判断是否显示该 Question。首先我们需要一行 import 语句：

```
polls/views.py¶
from django.utils import timezone
然后我们把 get_queryset 方法改写成下面这样：

polls/views.py¶
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```
Question.objects.filter(pub_date__lte=timezone.now())返回一个包含Question的pub_date小于或等于（即，早于或等于）timezone.now的时间查询集。

## 	测试新视图¶
启动服务器、在浏览器中加载站点、创建一些发布时间在过去和将来的 Questions，然后检验只有已经发布的 Questions 才会展示出来，现在你就可以对自己感到满意了。你不想修改每次可能与这相关的代码时都重复这样做——所以让我们基于以上shell 会话中的内容，再编写一个测试。

将下面的代码添加到polls/tests.py：

```
polls/tests.py¶
from django.urls import reverse
```
然后我们写一个公用的快捷函数来创建投票问题，再为视图创建一个测试类：

```
polls/tests.py

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```







	











