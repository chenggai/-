from django.contrib import admin

# Register your models here.
from App01.models import User
class UserAdmin(admin.ModelAdmin):
    #显示字段列表
    list_display=['pk','username','password']
    #分页
    list_per_page=5
    #搜索字段
    search_fields=['username']
    #过滤字段
    list_filter=['uid','username']
    #添加用户的时候，用户信息分组
    fieldssets=[
        ('基本信息',{'fields':['username']}),
        ('其他信息',{'fields':['password','email']}),
    ]

admin.site.register(User,UserAdmin)
