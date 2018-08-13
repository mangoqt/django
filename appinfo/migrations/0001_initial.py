# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('subsystem', models.CharField(max_length=50)),
                ('appname', models.CharField(max_length=200, null=True)),
                ('depapp', models.CharField(max_length=200)),
                ('port', models.CharField(max_length=50, null=True)),
                ('domain', models.CharField(max_length=500, null=True)),
                ('envrio', models.CharField(max_length=200)),
                ('create_tm', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'deviceinfo',
            },
        ),
    ]
