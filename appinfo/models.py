# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    subsystem = models.CharField(max_length=50)
    appname = models.CharField(max_length=200, null=True)
    depapp = models.CharField(max_length=200)
    port = models.CharField(max_length=50, null=True)
    domain = models.CharField(max_length=500, null=True)
    envrio = models.CharField(max_length=200)
    create_tm = models.DateTimeField(auto_now_add=True)

    #重命名表名
    class Meta:
        db_table='deviceinfo'

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (
        self.hostname, self.ip, self.subsystem, self.appname, self.depapp, self.port, self.domain, self.envrio)
