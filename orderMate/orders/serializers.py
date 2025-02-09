from rest_framework import serializers
from .models import Order, Dispatch, Received

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'

class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Received
        fields = '__all__'
