'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-21 20:01:53
FilePath: /whynot-Django/python222_site1/order/views.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''


from django.shortcuts import render
from django.urls import path
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse 
from django.urls import resolve


def index(request):
    route_url = reverse('order:index')
    print(route_url)
    result = resolve(route_url)
    # print(f"\n route_url:,{route_url},\n RESULT:,{result}")
    
    return HttpResponse("信息--Hello, world. You're at the order index.")


def list(request,year,month,day):
    args = [year,month,day]
    route_url = reverse('order:list',args=args)
    print(route_url)
    result = resolve(route_url)
    
    print(f"request:{request}\n 反向解析路由:,{route_url},\n  路由信息:,{result} \n ")
    
    return HttpResponse("订单列表")