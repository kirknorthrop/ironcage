# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20170618_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
