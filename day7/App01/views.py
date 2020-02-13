from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm
from App01.models import User


def register(request):
    if request.method == 'POST':
        # 验证数据
        #1 用提交过来的数据request.POST生成表单对象
        form = RegisterForm(request.POST)
        # 2 通过form的is_valid来检测数据是否合格，合格返回True，不合格返回False
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data)
            return HttpResponse("首页")
        else:
            print(form.errors)
            return render(request, 'App01/register.html', locals())
    else:
        return render(request,'App01/register.html')

def verify(request):

    if request.method=='POST':
        form=LoginForm(request.POST)
        #验证
        if form.is_valid():
            return HttpResponse("验证通过")
        else:
            return render(request,'App01/login.html')
    form=LoginForm()
    return render(request,'App01/login.html',locals())

def send_sms(request):
    from App01.SMS import sms
    from random import randint
    if request.is_ajax():
        phone=request.POST.get('phone')
        code=randint(1000,9999)
        request.session['code']=code
        request.session.set_expiry(5 * 60)  #5分钟内有效
        param="{'number':%d}" % code
        res=sms.send(phone,param)
        print(code,phone)
        return JsonResponse({'code':1})
    else:
        code=randint(1000,9999)
        param = "{'number':%d}" % code
        res = sms.send('13718234629', param)
        print(res)
        print(type(res))
        return HttpResponse(f'已发送{code}')

def sms_login(request):
    if request.method == 'POST':
        # 验证短信验证码
        yzm = request.POST.get('yzm')
        # 从session获取存入验证码
        code = str(request.session.get('code'))
        print(code, yzm)
        print(type(code), type(yzm))
        if yzm == code:
            return HttpResponse("验证成功")
    return render(request,'App01/sms.html')

