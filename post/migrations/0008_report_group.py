# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_report_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_group', to='post.Group'),
        ),
    ]
