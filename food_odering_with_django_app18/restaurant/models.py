from django.db import models


class Dish(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.IntegerField()

    image = models.ImageField(upload_to="dishes/")

    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name



class Order(models.Model):

    customer_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.customer_name



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.dish.name