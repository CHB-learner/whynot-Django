from django.db import models

# Create your models here.


# 映射数据库

class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=20)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'student_info'