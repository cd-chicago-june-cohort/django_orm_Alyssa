# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_auto_20170717_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
