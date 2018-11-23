# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='rating',
        ),
        migrations.AddField(
            model_name='ratings',
            name='content',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='ratings',
            name='design',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='ratings',
            name='usability',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]