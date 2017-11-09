# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]