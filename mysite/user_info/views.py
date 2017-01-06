#encoding=utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from user_info.models import user_info1
from hashlib import sha1
from  django.http  import JsonResponse
# Create your views here.
def index(request):
    uname = request.session.get('uname')
    print("-------------%s--------------"%uname)
    return render(request,'base.html',{'uname':uname})

def login(request):
    return render(request,'user_info/login.html',{'msg':None})

def register(request):
    return render(request,'user_info/register.html')

def registerHand(request):
    uname = request.POST.get('user_name')
    upasswad = request.POST.get('pwd')
    uemail = request.POST.get('email')

    s1 = sha1()
    s1.update(upasswad)
    upwd = s1.hexdigest()

    user = user_info1()
    user.uname = uname
    user.upwd = upwd
    user.ueamil = uemail
    user.save()
    return HttpResponseRedirect('/user_info/login/')

def loginHand(request):
    #根据name值，用POST方法获取传过来的值
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    check = request.POST.get('check')
    print(check)
    #将upwd进行加密
    s1 = sha1()
    s1.update(upwd)
    upwd1 = s1.hexdigest()

    #根据uname查询数据库
    try:
        user = user_info1.objects.get(uname=uname)

        # 如果密码和用户名都正确，就存入session和cookie
        if user.upwd == upwd1:
            if check == 1:
                print('-----------------------')
                request.set_cookie('uname', uname)
            request.session['uname'] = uname
            return redirect(reverse('user_info:index'))

        else:
            return render(request, 'user_info/login.html', {'msg': '密码不正确'})
    except Exception,e:
        return render(request, 'user_info/login.html', {'msg': '用户名不存在'})





def uname_verify(request):
    uname = request.POST.get('username')
    num = user_info1.objects.filter(uname=uname).count()
    list = {'num':num}
    return JsonResponse(list)



