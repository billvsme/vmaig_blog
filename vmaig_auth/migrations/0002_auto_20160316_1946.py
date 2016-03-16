# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmaig_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmaiguser',
            name='img',
            field=models.CharField(verbose_name='头像地址', default='/static/tx/default.jpg', max_length=200),
        ),
    ]
