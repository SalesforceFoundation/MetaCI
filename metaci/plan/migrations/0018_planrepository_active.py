# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-13 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("plan", "0016_auto_20180904_1457")]

    operations = [
        migrations.AddField(
            model_name="planrepository",
            name="active",
            field=models.BooleanField(default=True),
        )
    ]
