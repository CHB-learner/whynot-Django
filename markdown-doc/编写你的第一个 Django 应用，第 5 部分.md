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



