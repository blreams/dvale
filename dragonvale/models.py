# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=32)

class Currency(models.Model):
    name = models.CharField(max_length=32)

class Island(models.Model):
    name = models.CharField(max_length=32)
    cost_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    level_available = models.IntegerField(default=1)
    summon_time = models.DurationField()

class Habitat(models.Model):
    name = models.CharField(max_length=64)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    dragon_capacity = models.IntegerField(default=1)
    coffer_currency = models.ForeignKey(Currency, related_name='coffer_currencies', on_delete=models.CASCADE)
    coffer_capacity = models.IntegerField(default=1)
    length = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    cost_currency = models.ForeignKey(Currency, related_name='cost_currencies', on_delete=models.CASCADE)
    cost = models.IntegerField(default=1)
    build_time = models.DurationField()

