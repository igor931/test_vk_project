# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_post_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]