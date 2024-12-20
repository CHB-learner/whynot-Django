'''
Author: CHB-learner 211430209@mail.dhu.edu.cn
Date: 2024-12-11 15:31:49
FilePath: /whynot-Django/djangotutorial/polls/admin.py
Description: 

~请在这里写文件功能描述~


Copyright (c) 2024 by CHB-learner 211430209@mail.dhu.edu.cn, All Rights Reserved. 
'''
# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin

# from .models import Question,Choice

# admin.site.register(Question)
# admin.site.register(Choice)


# from django.contrib import admin

# from .models import Question


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


# admin.site.register(Question, QuestionAdmin)


##   Aleck 
##   123456

# from django.contrib import admin

# from .models import Question


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('question_text', {"fields": ["question_text"]}),
#         ("Date information_11", {"fields": ["pub_date"]}),
#     ]


# admin.site.register(Question, QuestionAdmin)



# from django.contrib import admin

# from .models import Choice, Question

# # ...
# admin.site.register(Choice)



from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]


admin.site.register(Question, QuestionAdmin)