#coding:utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/',views.Device_list,name='Device_list'),
    url(r'^result/',views.search,name='search'),
    url(r'^add/',views.add,name='add'),
    url(r'^dele/',views.dele,name='dele'),
    url(r'^choose/',views.choose,name='choose'),#获取要修改的记录
    url(r'^modify/',views.modify,name='modify')
]
