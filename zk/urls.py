#coding:utf-8
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^zkhost/',views.zklist,name='zkhost'),
    url(r'^addzk/',views.addzk,name='addzk'),
    url(r'^nodelist/',views.zknode,name='nodelist'),
]