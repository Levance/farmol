# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 13:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='\u6536\u8d27\u5730\u5740')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('person', models.CharField(max_length=100, verbose_name='\u6536\u8d27\u4eba')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u6536\u8d27\u5730\u5740',
                'verbose_name_plural': '\u6536\u8d27\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='\u6570\u91cf')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='\u5546\u54c1')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='UserOrderTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('1', '\u672a\u4ed8\u6b3e'), ('2', '\u5df2\u4ed8\u6b3e'), ('3', '\u5f85\u53d1\u8d27'), ('4', '\u5df2\u53d1\u8d27'), ('5', '\u5df2\u5b8c\u6210')], default=1, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('price', models.IntegerField(default=0, verbose_name='\u91d1\u989d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.UserAddress', verbose_name='\u6536\u8d27\u5730\u5740')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8ba2\u5355',
                'verbose_name_plural': '\u7528\u6237\u8ba2\u5355',
            },
        ),
        migrations.AddField(
            model_name='userorder',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.UserOrderTable', verbose_name='\u8ba2\u5355'),
        ),
    ]