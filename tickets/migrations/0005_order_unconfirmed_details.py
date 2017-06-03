# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 08:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20170530_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unconfirmed_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
