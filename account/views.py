# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.contrib.auth import *
# Create your views here.

def login_view(request):
    msg = []
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('../appinfo/list')
            else:
                msg.append("用户名错误")
        else:
            msg.append("登陆信息错误")
    return render(request,'account/login.html',{'errors': msg})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../account/login")
