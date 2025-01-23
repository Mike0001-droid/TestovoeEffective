from rest_framework import serializers
from .models import Order
from rest_framework.renderers import JSONRenderer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
