# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    type_id = models.IntegerField()
    weight = models.FloatField()
    stock = models.BooleanField()
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ('id',)

    # def __unicode__(self):
    #     return self.id


class Tag(models.Model):
    name = models.CharField(max_length=100)

    # def __unicode__(self):
    #     return self.name
