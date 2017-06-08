# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonvale', '0005_auto_20170608_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='element',
            options={'verbose_name_plural': '3. Elements'},
        ),
        migrations.AlterField(
            model_name='habitat',
            name='build_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='island',
            name='summon_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]