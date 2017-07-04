# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrix', '0005_metric_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='department',
            name='part_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='metrix.Category'),
        ),
    ]