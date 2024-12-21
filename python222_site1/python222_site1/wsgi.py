'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 11:31:31
FilePath: /whynot-Django/python222_site1/python222_site1/wsgi.py
Description: 

全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是
Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】
全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是
Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】
全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是
Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】
全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是
Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】
全 称 为 Python Web Server Gateway Interface，即Python服务器⽹关接⼝，是
Python应⽤与Web服务器之间的接⼝，⽤于Django项⽬在服务器上的部署和上线；【不用修改】


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
"""
WSGI config for python222_site1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python222_site1.settings')

application = get_wsgi_application()
