from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class Good(models.Model):
    goodID = models.IntegerField()
    goodName = models.CharField(max_length=100)
    goodInfo = models.TextField()
    goodNumber = models.IntegerField()
    goodPrice = models.FloatField()


class ShoppingCart(models.Model):
    orderID = models.IntegerField()
    username = models.CharField(max_length=20)
    goodsID = models.IntegerField()
    goodsNumber = models.IntegerField()


class Order(models.Model):
    orderID = models.IntegerField()
    logisticsID = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    price = models.FloatField()



