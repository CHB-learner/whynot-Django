'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-23 13:59:53
FilePath: /whynot-Django/python222_site1/helloWorld/admin.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.contrib import admin

# Register your models here.



from helloWorld.models import BookTypeInfo
# Register your models here.

# 方法一，将模型直接注册到admin后台
admin.site.register(BookTypeInfo)