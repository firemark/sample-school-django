# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='cor_x',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='cor_y',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True),
        ),
    ]
