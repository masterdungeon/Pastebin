# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0002_auto_20180415_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='url',
            field=models.CharField(default=uuid.uuid1, max_length=32, unique=True),
        ),
    ]
