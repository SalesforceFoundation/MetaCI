# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='github_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]