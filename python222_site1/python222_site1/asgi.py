'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 11:31:31
FilePath: /whynot-Django/python222_site1/python222_site1/asgi.py
Description: 

开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】
开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】
开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】
开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】
开启⼀个ASGI服务，ASGI是异步⽹关协议接⼝；【不用修改】


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
"""
ASGI config for python222_site1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python222_site1.settings')

application = get_asgi_application()
