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