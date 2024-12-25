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
# admin.site.register(BookTypeInfo)

from helloWorld.models import BookInfo
from django.contrib import admin
# 方法二，自定义类，继承ModelAdmin
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'bookName', 'price', 'publishDate', 'bookType']
    search_fields = ['bookName']
    
    # 重写分类方法，设置只读字段
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['bookName']
        return self.readonly_fields


# 设置网站标题和应用标题
admin.site.site_title = 'AAA管理系统'
admin.site.site_header = 'BBB管理系统'
admin.site.index_title = 'CCC管理系统'
