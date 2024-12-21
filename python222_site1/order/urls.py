from django.shortcuts import render
from django.urls import path
from django.contrib import admin


import order.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', order.views.index,name='index'),
    path('list/<int:year>/<int:month>/<int:day>/', order.views.list,name='list'),
]
