# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 09:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_requested', models.IntegerField()),
                ('would_like_ticket_set_aside', models.BooleanField()),
                ('thu', models.BooleanField()),
                ('fri', models.BooleanField()),
                ('sat', models.BooleanField()),
                ('sun', models.BooleanField()),
                ('mon', models.BooleanField()),
                ('about_you', models.TextField()),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grant_application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]