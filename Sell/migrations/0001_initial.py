# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodID', models.IntegerField()),
                ('goodName', models.CharField(max_length=100)),
                ('goodInfo', models.TextField()),
                ('goodNumber', models.IntegerField()),
                ('goodPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderID', models.IntegerField()),
                ('logisticsID', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderID', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('goodsID', models.IntegerField()),
                ('goodsNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
