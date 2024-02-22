from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code','phone_number', 'user', 'created']
        read_only_fields = ('user',)  # Prevent the API consumer from setting the `user` field directly


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'budget', 'time']
