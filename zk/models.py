# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Zk_host(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    create_time=models.DateField(auto_now_add=True)

    class Meta:
        db_table='zk_host'

    def __unicode__(self):
        return u"%s %s  "%(self.name,self.ip)

class Zk_node(models.Model):
    app_code = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    zk_id = models.ForeignKey(Zk_host,on_delete=models.CASCADE)
    is_sync = models.IntegerField()
    deleted = models.IntegerField()
    sync_time= models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'zk_node'

    def __unicode__(self):
        return u'%s %s %s %s '%(self.app_code,self.path,self.content,self.zk_id)