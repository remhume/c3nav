# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-04 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='depends',
            field=models.ManyToManyField(to='mapdata.Package'),
        ),
    ]
