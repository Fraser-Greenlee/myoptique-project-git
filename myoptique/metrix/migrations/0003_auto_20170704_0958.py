# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrix', '0002_metric_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='score',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='value',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='weight',
        ),
        migrations.AddField(
            model_name='department',
            name='part_of',
            field=models.CharField(default='ehh', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metric',
            name='curr_val',
            field=models.IntegerField(default=0),
        ),
    ]