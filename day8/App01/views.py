import os

from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader

from day08.settings import MEDIA_ROOT, EMAIL_HOST_USER


def do_upload(request):
    if request.method=='POST':
        #1、获取文件上传对象
        file_obj=request.FILES.get('photo')

        #检验上传文件是否符合要求
        from App01.uploadfile import Upload
        fupload=Upload(MEDIA_ROOT,ext=['jpg','jpeg','png'])
        res=fupload.load(file_obj)
        if isinstance(res,str):
            return HttpResponse(res)
        else:
            return HttpResponse('上传成功')

    return render(request,'App01/upload.html')


def send_one(request):
    send_mail('加油','房子',EMAIL_HOST_USER,['515269984@qq.com'])
    return HttpResponse('发送一封成功')

def send_many(request):
    # mail1=('油','房子',EMAIL_HOST_USER,['515269984@qq.com'])
    # mail2 = ('买油', '房子', EMAIL_HOST_USER, ['chenggai0310@126.com'])
    # send_mass_mail((mail1,mail2))

    # 发送html邮件
    subject1, from_mail, to = ("女足", EMAIL_HOST_USER, ['313728420@qq.com'])
    content = loader.get_template("app01/sport.html").render()
    obj = EmailMultiAlternatives(subject1, from_email=from_mail, to=to)
    obj.attach_alternative(content, 'text/html')
    obj.send()
    return HttpResponse('发送多封成功')

def edit(request):
    if request.method=='POST':
        content=request.POST.get('content')
        return HttpResponse(content)
    return render(request,'App01/edit.html')


