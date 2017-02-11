from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    def __unicode__(self):
    	return self.name
    name = models.CharField(max_length=200)

   
    class Meta:
        ordering = ('name',)

class Item(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=500)
    image = models.ImageField( max_length=100)
    brand = models.CharField(max_length=200)
    size = models.CharField(max_length=4)
    url = models.CharField(max_length=500)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('name',)