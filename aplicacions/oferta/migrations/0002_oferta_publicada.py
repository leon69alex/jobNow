# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]