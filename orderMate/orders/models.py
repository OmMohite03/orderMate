from django.db import models
from users.models import User

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)
    model_no = models.CharField(max_length=50)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_id} - {self.model_no}"


class Dispatch(models.Model):
    dispatch_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    dispatch_person = models.CharField(max_length=100)
    dispatch_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispatch {self.dispatch_id} for Order {self.order.order_id}"


class Received(models.Model):
    received_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    received_person = models.CharField(max_length=100)
    received_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Received {self.received_id} for Order {self.order.order_id}"
