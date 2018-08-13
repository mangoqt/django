# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from .models import *
from kazoo.client import *
# Create your views here.
#zk主机
def zklist(request):
    hostlist = Zk_host.objects.order_by('-id')
    return render(request,'zk/list.html',locals())

def addzk(request):
    if request.POST:
        name = request.POST['name']
        ip = request.POST['ip']
        port=request.POST['port']
        Zk_host.objects.create(name=name,ip=ip,port=port)
       #return  HttpResponseRedirect('zk/zkhost')
    return render(request,'zk/hostadd.html',locals())


#zk节点

def zknode(request):
    nodelist = Zk_node.objects.order_by('-id')
    return render(request,'zk/nodeindex.html',locals())


