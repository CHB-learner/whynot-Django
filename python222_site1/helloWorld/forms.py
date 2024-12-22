from django.forms import ModelForm
from helloWorld.models import StudentInfo
# 定义学生表单类

class StudentForm(ModelForm):
    model = StudentInfo     # 指定数据模型
    fields  = '__all__'     # 指定表单字段
    