'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-23 13:59:53
FilePath: /whynot-Django/python222_site1/helloWorld/models.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.db import models

# Create your models here.


# 映射数据库

class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=20)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'student_info'
        
        
class BookTypeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    bookTypeName = models.CharField(max_length=20)
    class Meta:
        db_table = "t_bookType"
        verbose_name = "图书类别信息" # 给模型取个直观的名字
    
    def __str__(self): # 重写__str__方法
        # 返回图书类别名称
        return  self.bookTypeName

class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=20)
    price = models.FloatField()
    publishDate = models.DateField()
    bookType = models.ForeignKey(BookTypeInfo, on_delete=models.PROTECT)
    class Meta:
        db_table = "t_book"
        verbose_name = "图书信息" # 给模型取个直观的名字
    


    
class AccountInfo(models.Model):
    user = models.CharField(max_length=20)
    account = models.FloatField()
    class Meta:
        db_table = "t_account"
        verbose_name = "用户账户信息" # 给模型取个直观的名字