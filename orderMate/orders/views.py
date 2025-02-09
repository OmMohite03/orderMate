from rest_framework import viewsets
from .models import Order, Dispatch, Received
from .serializers import OrderSerializer, DispatchSerializer, ReceivedSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class ReceivedViewSet(viewsets.ModelViewSet):
    queryset = Received.objects.all()
    serializer_class = ReceivedSerializer
