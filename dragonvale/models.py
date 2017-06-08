# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class ElementType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = '1. ElementTypes'

@python_2_unicode_compatible
class Currency(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = '2. Currencies'

@python_2_unicode_compatible
class Element(models.Model):
    name = models.CharField(max_length=32)
    element_type = models.ForeignKey(ElementType, blank=True, null=True, on_delete=models.CASCADE)
    opposite_element = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        #ordering = ['name', 'element_type', 'opposite_element']
        verbose_name_plural = '3. Elements'

@python_2_unicode_compatible
class Island(models.Model):
    name = models.CharField(max_length=32)
    cost_currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    level_available = models.IntegerField(default=1)
    summon_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'cost_currency', 'cost', 'level_available', 'summon_time']
        verbose_name_plural = '4. Islands'

@python_2_unicode_compatible
class Habitat(models.Model):
    name = models.CharField(max_length=64)
    element = models.ForeignKey(Element, blank=True, null=True, on_delete=models.CASCADE)
    dragon_capacity = models.IntegerField(default=1)
    coffer_currency = models.ForeignKey(Currency, related_name='coffer_currencies', blank=True, null=True, on_delete=models.CASCADE)
    coffer_capacity = models.IntegerField(default=1)
    length = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    cost_currency = models.ForeignKey(Currency, related_name='cost_currencies', blank=True, null=True, on_delete=models.CASCADE)
    cost = models.IntegerField(default=1)
    build_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'element', 'dragon_capacity', 'coffer_currency', 'length', 'width', 'cost_currency', 'cost', 'build_time']
        verbose_name_plural = '5. Habitats'

