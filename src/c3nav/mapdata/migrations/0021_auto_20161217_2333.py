# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0020_auto_20161216_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevatorlevel',
            name='override_altitude',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='override level altitude'),
        ),
        migrations.AlterField(
            model_name='level',
            name='altitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, unique=True, verbose_name='level altitude'),
            preserve_default=False,
        ),
    ]
