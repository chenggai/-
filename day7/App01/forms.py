# 自定义表单
from django import forms
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from App01.models import User


# def check_password(value):
#     """
#     验证密码是不是纯数字
#     :param value: 密码字符串
#     :return: 无
#     """
#     if re.match(r'\d*$',value,re.I):
#         raise ValidationError("密码不能是纯数字")


# 注册表单 表单主要是针对html中表单提交的数据进行验证
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',min_length=3,required=True,
                                error_messages={'required':'用户名必须输入','min_length':'用户名长度不能小于3'}
                               )
    password = forms.CharField(min_length=3,
                               required=True,
                               validators=[RegexValidator(regex=r'\d*$', message="密码不能是纯数字",code='password')],  # 自定义验证函数
                               error_messages={'required':'密码必须输入','min_length':'密码长度必须大于3'}
                               )
    confirm_password = forms.CharField(min_length=3,
                               required=True,
                               error_messages={'required': '密码必须输入', 'min_length': '密码长度必须大于3'}
                               )
    email = forms.EmailField(error_messages={'invalid':'邮箱格式不正确'})

    # 单个字段的验证方法
    # 方法的名称格式：clean_字段名()
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 查询数据库
        # 如果存在
        if User.objects.filter(username=username).first():
            raise ValidationError("用户名重复")
        # 必须把正确数据返回
        return username

    # 全局验证，涉及多个字段
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # 判断两者是否相等
        if password != confirm_password:
            raise ValidationError({'confirm_password':["两次密码输入不一致"]})
        return self.cleaned_data


#登录
class LoginForm(forms.Form):
    username=forms.CharField(required=True,error_messages={
        'required':'用户名必须输入'
    })
    password=forms.CharField()
    captcha=CaptchaField()   #验证码字段

