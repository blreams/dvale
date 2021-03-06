# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonvale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('dragon_capacity', models.IntegerField(default=1)),
                ('coffer_capacity', models.IntegerField(default=1)),
                ('length', models.IntegerField(default=1)),
                ('width', models.IntegerField(default=1)),
                ('cost', models.IntegerField(default=1)),
                ('build_time', models.DurationField()),
                ('coffer_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffer_currencies', to='dragonvale.Currency')),
                ('cost_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_currencies', to='dragonvale.Currency')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonvale.Element')),
            ],
        ),
        migrations.RemoveField(
            model_name='island',
            name='reward',
        ),
        migrations.RemoveField(
            model_name='island',
            name='reward_currency',
        ),
        migrations.AlterField(
            model_name='island',
            name='cost_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonvale.Currency'),
        ),
    ]
