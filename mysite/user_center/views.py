#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from user_info.models import *

# Create your views here.

# ============================= user center info page view  ==================================
def ucInfo(request):
    value = user_info1.objects.filter(id=1)
    print(type(value))
    for i in value:
        print(i.uname)
        print(i.upwd)
    context = {'value':value}
    return render(request,'user_center/user_center_info.html',context)


# ============================= user center address page view  =================================
def ucAddress(request):
    return render(request,'user_center/user_center_site.html')

# 获取表单中的数据
def getAddressInfo(request):
    if request.method == 'POST':
        site_name = request.POST['uc_name']
        site_zip = request.POST['uc_zip']
        site_site = request.POST['uc_site']
        site_phone = request.POST['uc_phone']

        # print(site_name+site_site+site_zip+site_phone)

        # 添加数据到数据库
        meter = userCenter()
        meter.uc_name = site_name
        meter.uc_address = site_site
        meter.uc_zipcode = site_zip
        meter.uc_phone = site_phone

        meter.uc_user_id = 1  # 这个数据需要交互

        '''
        这个数据要和负责登陆的沟通,当前登陆的是谁 , 他会存储在session里面, 取登陆用户信息就可以了, 如果存储
        的是 user,就是 这个等式 , 如果他存储的是 id , 那么就用 mater.uc_user_id = 登陆用户的 ID
        '''

        meter.save()

        return HttpResponse('ok')
    else:
        return HttpResponse('error')