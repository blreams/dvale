# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonvale', '0004_auto_20170608_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='element',
            options={'ordering': ['name', 'element_type', 'opposite_element'], 'verbose_name_plural': '3. Elements'},
        ),
        migrations.RemoveField(
            model_name='element',
            name='opposite_element_type',
        ),
        migrations.AddField(
            model_name='element',
            name='opposite_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonvale.Element'),
        ),
        migrations.AlterField(
            model_name='element',
            name='element_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonvale.ElementType'),
        ),
    ]