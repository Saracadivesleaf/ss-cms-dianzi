# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0002_auto_20141015_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='project_time',
            field=models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
