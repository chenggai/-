from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from App.forms import RegisterForm
from App.models import User
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        #生成响应对像
        res=HttpResponse('cookie')
        res.set_cookie('username',username,max_age=3*60*60)
        print(res)
        return res
    return render(request,'login.html')

def reply(request):
    # 获取cookie中的username键值对
    username = request.COOKIES.get('username')
    # username不为空就是登录过，否则未登录
    if username:
        return HttpResponse("发表评论")
    else:
        return redirect(reverse("App:login"))


def index(request):
    # 获取cookie
    username = request.COOKIES.get('username')
    print(username)
    return render(request,'index.html',context={'username':username})


def logout(request):
    # 生成响应对象HttpResponseRedirect
    res = redirect(reverse("App:home"))
    print(res)
    res.delete_cookie('username')
    return res

def register(request):
    if request.method=='POST':
        #验证数据
        #1、用提交过来的数据request.POST生成表单对象
        form=RegisterForm(request.POST)
        #2、通过form的is_valid来检测数据是否合格，合格返回True，不合格返回False
        if form.is_valid():
            print(form.cleaned_data)
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            user=User(username=username,password=password,email=email,phone=phone)
            user.save()
            return HttpResponse('首页')
        else:
            return render(request,'register.html',locals())
    else:
        #get请求
        return render(request,'register.html')