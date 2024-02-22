from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User, Customer, Order

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(User, UserAdmin)

