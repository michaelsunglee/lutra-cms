# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('page_number', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
