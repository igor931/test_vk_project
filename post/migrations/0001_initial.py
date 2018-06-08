# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-16 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(null=True)),
                ('text', models.TextField()),
                ('url', models.URLField()),
                ('comments', models.PositiveIntegerField()),
                ('likes', models.PositiveIntegerField()),
                ('reposts', models.PositiveIntegerField()),
                ('views', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='post.Group')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
