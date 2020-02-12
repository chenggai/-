# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/15 9:08
# @Author  :
# @QQ

from django.contrib import admin
from django.urls import path

from App import views
#写上app_name
app_name='App'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('mark/',views.reply,name='mark'),
    path('home/',views.index,name='home'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
]