# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_session_commission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, max_length=1000)),
                ('isAnonymous', models.BooleanField(default=True)),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.Session')),
            ],
        ),
    ]