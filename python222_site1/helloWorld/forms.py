'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-23 13:59:53
FilePath: /whynot-Django/python222_site1/helloWorld/forms.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.forms import ModelForm
from helloWorld.models import StudentInfo
from django import forms

# 定义学生表单类

class StudentForm(ModelForm):
    class Meta:
        model = StudentInfo     # 指定数据模型
        fields  = '__all__'     # 指定表单字段
        
        
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name','Class':'inputClass'}),   
            'age': forms.NumberInput(attrs={'id': 'age'})   
        }
        
        labels = {
            'name': '姓名',
            'age': '年龄'
        }

from django.forms import Form
from helloWorld.models import BookTypeInfo
# class BookInfoForm(Form):
#     """
#     图书表单
#     """
#     bookName = forms.CharField(max_length=20, label="图书名称")
#     price = forms.FloatField(label="图书价格")
#     publishDate = forms.DateField(label="出版日期")
#     # 获取图书类别列表
#     bookTypeList = BookTypeInfo.objects.values()
#     # 图书类别以下拉框形式显示，下拉框选项id是图书类别Id，下拉框选项文本是图书类别名称
#     choices = [(v['id'], v['bookTypeName']) for v, v in enumerate(bookTypeList)]
#     bookType_id = forms.ChoiceField(required=False, choices=choices, label="图书类别")

from django.forms import Form
from django.forms import widgets
class BookInfoForm(Form):
    """
    图书表单
    """
    bookName = forms.CharField(
    max_length=20,
    label="图书名称",
    required=True,
    widget=widgets.TextInput(attrs={"placeholder": "请输入用户名",
    "class": "inputCls"})
    )
    price = forms.FloatField(label="图书价格")
    publishDate = forms.DateField(label="出版日期")
    # 获取图书类别列表
    bookTypeList = BookTypeInfo.objects.values()
    # 图书类别以下拉框形式显示，下拉框选项id是图书类别Id，下拉框选项文本是图书类别名称
    choices = [(v['id'], v['bookTypeName']) for v, v in
    enumerate(bookTypeList)]
    bookType_id = forms.ChoiceField(required=False, choices=choices,
    label="图书类别")


from helloWorld.models import BookInfo
class BookInfoModelForm(ModelForm):
    # 配置中心
    class Meta:
        model = BookInfo # 导入model
        fields = '__all__' # 代表所有字段
        # fields = ['bookName', 'price'] # 指定字段
        widgets = { # 定义控件
        'bookName': forms.TextInput(attrs={"placeholder": "请输入用户名",
        'id': 'bookName', 'class': 'inputCls'})
        }
        labels = { # 指定标签
        'bookName': '图书名称',
        'price': '图书价格',
        'publishDate': '出版日期',
        'bookType': '图书类别'
        }
        help_texts = {
        'bookName': '请输入图书名称'
        }