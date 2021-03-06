# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161012_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
