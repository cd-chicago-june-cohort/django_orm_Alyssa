# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0002_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]