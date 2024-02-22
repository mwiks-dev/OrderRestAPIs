from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    pass
    def __str__(self):
            return self.email

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    code = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, default='0114680821')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    item = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)