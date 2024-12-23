'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-23 15:11:37
FilePath: /whynot-Django/python222_site1/helloWorld/Jinja3.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)

    env.globals.update(
    {
    'static': staticfiles_storage.url,
    'url': reverse
    }
    )
    return env

