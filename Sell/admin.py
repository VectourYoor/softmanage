from django.contrib import admin
from Sell.models import *


class GoodList(admin.ModelAdmin):
    list_display = ('goodID', 'goodName', 'goodNumber', 'goodPrice')


class UserList(admin.ModelAdmin):
    list_display = ('username', 'phoneNumber', 'address')


class OrderList(admin.ModelAdmin):
    list_display = ('orderID', 'logisticsID', 'username')


admin.site.register(User, UserList)
admin.site.register(Good, GoodList)
admin.site.register(ShoppingCart)
admin.site.register(Order, OrderList)
