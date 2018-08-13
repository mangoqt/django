# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.core.paginator import *
from django.db.models.aggregates import Count  # 计算总数
from django.contrib.auth.decorators import login_required #权限认证
from .models import Device

import logging
logger = logging.getLogger("django")

# Create your views here.
# 列表信息
@login_required  #权限装饰器
def Device_list(request):
    count_dict = Device.objects.aggregate(id_count=Count('id'))  # 统计count记录
    count = count_dict['id_count']
    limit = 15  # 每页显示的记录数
    device_list = Device.objects.order_by('-id')  # 查找数据库记录
    paginator = Paginator(device_list, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        device_list = paginator.page(page)  # 获取某页对应记录
    except PageNotAnInteger:  # 如果页码不是整数
        device_list = paginator.page(1)  # 取第一页记录
    except EmptyPage:  # 如果页码太大，每页相应记录
        device_list = paginator.page(paginator.num_pages)  # 取最后一页记录
    return render(request, 'appinfo/index.html', {'device_list': device_list, 'count': count})


# 查询
@login_required
def search(request):
    error_msg = []
    if request.POST:
        hostname=request.POST['hostname']
        ip = request.POST['ip']
        subsystem = request.POST['subsystem']
        appname = request.POST['appname']
        envrio = request.POST['envrio']

        device_list = Device.objects.filter(hostname__icontains=hostname).filter(ip__icontains=ip).filter(subsystem__icontains=subsystem).filter(appname__icontains=appname).filter(envrio__icontains=envrio).order_by('-id')
        count_dict = Device.objects.aggregate(id_count=Count(device_list))
        count = count_dict['id_count']
        limit = 15
        paginator = Paginator(device_list, limit)
        page = request.GET.get('page')
        try:
            device_list = paginator.page(page)
        except PageNotAnInteger:
            device_list = paginator.page(1)
        except EmptyPage:
            device_list = paginator.page(paginator.num_pages)
    return render(request, 'appinfo/index.html', locals())


# 新增
@login_required
def add(request):
    error_msg = []
    success_msg = []
    if request.POST:
        hostname = request.POST['hostname']
        ip = request.POST['ip']
        subsystem = request.POST['subsystem']
        appname = request.POST['appname']
        depapp = request.POST['depapp']
        port = request.POST['port']
        domain = request.POST['domain']
        envrio = request.POST['envrio']
        if (hostname.strip() == "" or ip.strip() == "" or subsystem.strip() == "" or appname.strip() == ""
            or depapp.strip() == "" or envrio.strip() == ""):
            error_msg.append("新增失败,域名和端口可不填，其他选项必填,请补充信息，然后保存，不填写直接返回")
        else:
            Device.objects.create(hostname=hostname, ip=ip, subsystem=subsystem, appname=appname,
                                  depapp=depapp, port=port, domain=domain, envrio=envrio)
            success_msg.append("新增成功")

    return render(request, 'appinfo/add.html', locals())


# 删除
@login_required
def dele(request):
    id_list = request.POST.getlist('post_id')
    for id in id_list:
        sqldelete=Device.objects.filter(id=id).delete()
    return HttpResponseRedirect('../list/')
    return render(request, 'appinfo/index.html', locals())


# 修改 choose函数先通过id获取要修改的信息，再通过modify函数修改保存
@login_required
def choose(request):
    id = request.POST.getlist('post_id')
    for i in id:
        chooseList = Device.objects.get(id=i)
    return render(request, 'appinfo/modify.html', locals())


@login_required
def modify(request):
    id = request.POST['id']
    hostname = request.POST['hostname']
    ip = request.POST['ip']
    subsystem = request.POST['subsystem']
    appname = request.POST['appname']
    depapp = request.POST['depapp']
    port = request.POST['port']
    domain = request.POST['domain']
    envrio = request.POST['envrio']
    Device.objects.filter(id=id).update(hostname=hostname, ip=ip, subsystem=subsystem, appname=appname,
                                        depapp=depapp, port=port, domain=domain, envrio=envrio)
    return render(request, 'appinfo/modify.html', locals())
