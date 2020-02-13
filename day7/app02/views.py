from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from day07.settings import COUNT_OF_PAGE
from app02.models import User


def list(request,page=1):
   data=User.objects.all()
   #生成分页器
   paginator=Paginator(data,COUNT_OF_PAEG)
   #获取分页对象
   pager=paginator.page(int(page))
   return render(request,'app02/list.html',context={
      'pages':pager,
      'page_range':paginator.page_range
   })