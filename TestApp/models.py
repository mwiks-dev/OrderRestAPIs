from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 10)
    code = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    item = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)