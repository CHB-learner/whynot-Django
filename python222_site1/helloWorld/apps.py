'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-23 13:59:53
FilePath: /whynot-Django/python222_site1/helloWorld/apps.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
from django.apps import AppConfig


class HelloworldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'helloWorld'
    verbose_name = "图书管理系统"
