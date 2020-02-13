"""day07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App01 import views
app_name = 'App01'
urlpatterns = [
    path('register/',views.register,name='register'),
    #第三方验证码
    path('verify/', views.verify, name='verify'),
    #发送短信验证码
    path('sms/', views.send_sms, name='sms'),
    #短信登录
    path('smslogin/', views.sms_login, name='smslogin'),
]
