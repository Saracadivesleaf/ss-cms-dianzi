# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='project_person_in_charge',
            field=models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba'),
        ),
    ]
