# -*- coding: utf-8 -*-
# @File    : forms.py
# 描述     ：
# @Time    : 2020/2/11 15:00
# @Author  :
# @QQ
from django import forms
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from App.models import User

def check_password(value):
    #re.I此匹配模式表示忽略大小写的情况下进行匹配
    if re.match(r'\d*$',value,re.I):
        raise ValidationError('密码不能是纯数字')

def check_phone(value):
    #re.I此匹配模式表示忽略大小写的情况下进行匹配
    if re.match(r'^1[3|4|5|7|8][0-9]{8}$',value):
        raise ValidationError('手机号格式有误')

# 注册表单，主要是针对html中表单提交的数据进行验证
class RegisterForm(forms.Form):
    username=forms.CharField(min_length=6,required=True,error_messages={'required':'用户名必须输入','min_length':'用户名长度不能小于6'})
    password=forms.CharField(min_length=6,max_length=12,required=True,
                             validators=[check_password],  #自定义验证函数
                             error_messages={'required': '密码必须输入', 'min_length':'密码长度不能小于6','max_length':'密码长度不能大于12'}
                             )
    confirm_password = forms.CharField(min_length=6, max_length=12, required=True,
                                       error_messages={'required': '密码必须输入', 'min_length': '密码长度不能小于6',
                                              'max_length': '密码长度不能大于12'}
                               )
    email=forms.EmailField(error_messages={'invalid':'邮箱格式不正确'})
    phone=forms.CharField(required=True,
                          validators=[check_phone],
                          error_messages={'required':'手机号必须输入'}
                          )

    #单个字段的验证方法
    #方法的名称格式：clean_字段名
    def clean_username(self):
        #获取用户名
        username=self.cleaned_data.get('username')
        #查询数据库
        #如果存在
        if User.objects.filter(username=username).first():
            raise ValidationError('用户名重复')

        #必须把正确数据返回
        return username

    #全局验证，设计多个字段
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        #判断两者是否相等
        if password != confirm_password:
            #全局验证需给个提示字段，方便知道有误地方
            raise ValidationError({'confirm_password':["两次密码输入不一致"]})
        return self.cleaned_data