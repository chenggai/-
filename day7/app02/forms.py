# 自定义表单
import re

from django import forms
from django.core.exceptions import ValidationError

from App01.models import User


def check_password(value):
    '''
    验证密码是不是纯数字
    :param value: 密码字符串
    :return:
    '''
    if re.match(r'\d*$',value,re.I):
        raise ValidationError('密码不能是纯数字')


# 注册表单，表单主要针对html中表单提交过来的数据进行验证
class RegisterForm(forms.Form):
    username=forms.CharField(label='用户名',min_length=3,required=True,
                             error_messages={'required':'请输入用户名','min_length':'长度最少3个字符'})
    password=forms.CharField(label='密码',min_length=3,required=True,
                             validators=[check_password],  # 自定义验证函数
                             error_messages={'min_length':'密码长度不能小于3','required':'密码不能为空'}
                                 )
    confirm_password = forms.CharField(label='验证密码',min_length=3, required=True,
                               error_messages={'min_length': '密码长度不能小于3', 'required': '密码不能为空'}
                               )
    email=forms.EmailField(error_messages={'invalid':'邮箱格式不正确'})

    #单个字段验证方法,必须以clean_开头+验证的字段名
    def clean_username(self):
        #获取用户名
        username=self.cleaned_data.get('username')
        # 查询数据库
        if User.objects.filter(username=username).first():
            raise ValidationError('用户名重复')
        #必须把正确数据返回
        return username

    #全局验证，涉及多个字段，必须使用clean
    def clean(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')

        #两者判等
        if password!=confirm_password:
            raise ValidationError('两次密码不一致')
        #必须返回所有验证过的数据
        return self.cleaned_data

