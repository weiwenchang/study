from django.shortcuts import render
from django.http import HttpResponse
from user_info.models import user_info1
# Create your views here.
def login(request):
    return render(request,'user_info/login.html')

def register(request):
    return render(request,'user_info/register.html')

def registerHand(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    uemail = request.POST.get('email')
    user = user_info1()
    user.uname = uname
    user.upwd = upwd
    user.ueamil = uemail
    user.save()
    return HttpResponse('HELLO')
