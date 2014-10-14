# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=30, verbose_name='\u7c7b\u522b\u540d')),
                ('parent_category', models.ForeignKey(verbose_name='\u7236\u7c7b\u522b', blank=True, to='category.Category', null=True)),
            ],
            options={
                'verbose_name': '\u7c7b\u522b',
                'verbose_name_plural': '\u7c7b\u522b',
            },
            bases=(models.Model,),
        ),
    ]
