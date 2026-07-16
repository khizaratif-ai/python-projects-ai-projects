from django.contrib import admin

from .models import Dish, Order, OrderItem


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "available"
    )

    list_editable = (
        "available",
    )



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "phone",
        "created_at"
    )



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "dish",
        "quantity"
    )