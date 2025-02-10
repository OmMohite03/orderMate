import json
from rest_framework import viewsets
from orders.models import Order, Dispatch, Received
from orders.serializers import OrderSerializer, DispatchSerializer, ReceivedSerializer
from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict

# API ViewSets
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class ReceivedViewSet(viewsets.ModelViewSet):
    queryset = Received.objects.all()
    serializer_class = ReceivedSerializer

# Monthly summary JSON API
def monthly_summary(request):
    data = defaultdict(lambda: {"orders": 0, "dispatches": 0, "received": 0})

    for order in Order.objects.all():
        month = order.order_date_time.strftime("%Y-%m")
        data[month]["orders"] += 1

    for dispatch in Dispatch.objects.all():
        month = dispatch.dispatch_date_time.strftime("%Y-%m")
        data[month]["dispatches"] += 1

    for received in Received.objects.all():
        month = received.received_date_time.strftime("%Y-%m")
        data[month]["received"] += 1

    return JsonResponse(data)

# HTML Page for Monthly Summary
def monthly_summary_page(request):
    # Fetch JSON response from the summary API
    from django.http import JsonResponse
    from .views import monthly_summary
    
    response = monthly_summary(request)
    data = json.loads(response.content.decode('utf-8'))

    return render(request, "orders/summary.html", {"data": data})