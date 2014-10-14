# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_person_in_charge', models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u79d1\u5b66\u7814\u7a76',
                'verbose_name_plural': '\u79d1\u5b66\u7814\u7a76',
            },
            bases=(models.Model,),
        ),
    ]
