from django.db.models.functions import TruncMonth
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Dispatch, Received
import requests
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer, ReceivedSerializer, DispatchSerializer
from django.shortcuts import get_object_or_404, redirect, render

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class ReceivedViewSet(viewsets.ModelViewSet):
    queryset = Received.objects.all()
    serializer_class = ReceivedSerializer

@api_view(['GET'])
def monthly_summary(request):
    orders_by_month = (
        Order.objects.annotate(month=TruncMonth('order_date_time'))
        .values('month')
        .annotate(order_count=Count('order_id'))
        .order_by('month')
    )

    dispatches_by_month = (
        Dispatch.objects.annotate(month=TruncMonth('dispatch_date_time'))
        .values('month')
        .annotate(dispatch_count=Count('dispatch_id'))
        .order_by('month')
    )

    received_by_month = (
        Received.objects.annotate(month=TruncMonth('received_date_time'))
        .values('month')
        .annotate(received_count=Count('received_id'))
        .order_by('month')
    )

    # Merging the results
    summary = {}
    for entry in orders_by_month:
        month = entry["month"].strftime('%Y-%m')
        summary.setdefault(month, {'orders': 0, 'dispatches': 0, 'received': 0})
        summary[month]['orders'] = entry['order_count']

    for entry in dispatches_by_month:
        month = entry["month"].strftime('%Y-%m')
        summary.setdefault(month, {'orders': 0, 'dispatches': 0, 'received': 0})
        summary[month]['dispatches'] = entry['dispatch_count']

    for entry in received_by_month:
        month = entry["month"].strftime('%Y-%m')
        summary.setdefault(month, {'orders': 0, 'dispatches': 0, 'received': 0})
        summary[month]['received'] = entry['received_count']

    from django.shortcuts import render


    return Response(summary)

def monthly_summary_page(request):
    api_url = "http://127.0.0.1:8000/api/summary/"
    response = requests.get(api_url)
    data = response.json() if response.status_code == 200 else {}

    return render(request, "summary.html", {"data": data})
