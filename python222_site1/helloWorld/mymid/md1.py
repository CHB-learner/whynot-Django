'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 16:29:23
FilePath: /whynot-Django/python222_site1/helloWorld/mymid/md1.py
Description: 

自定义中间件


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''

from django.utils.deprecation import MiddlewareMixin

class Md1(MiddlewareMixin):
    def process_request(self, request):
        print('request请求来了')
        return None

    def process_response(self, request, response):
        print('请求处理完毕')
        return response


