# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=30, null=True, verbose_name='\u4f5c\u8005', blank=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9')),
                ('page_view', models.IntegerField(null=True, verbose_name='\u8bbf\u95ee\u91cf')),
                ('classify', models.ForeignKey(verbose_name='\u5206\u7c7b', to='category.Category')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
    ]
