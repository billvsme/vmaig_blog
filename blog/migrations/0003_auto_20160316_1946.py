# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150514_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.CharField(default='/static/img/article/default.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.CharField(verbose_name='轮播图片', default='/static/img/carousel/default.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0),
        ),
        migrations.AlterField(
            model_name='column',
            name='status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0),
        ),
        migrations.AlterField(
            model_name='nav',
            name='status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_from',
            field=models.IntegerField(verbose_name='来源', choices=[(0, 'oschina'), (1, 'chiphell'), (2, 'freebuf'), (3, 'cnBeta')], default=0),
        ),
    ]
