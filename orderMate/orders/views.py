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

def monthly_summary(request):
    """
    Fetches summary of orders, dispatches, and received records month-wise.
    If a specific month (YYYY-MM) is provided as a query parameter, fetch only that month.
    """
    selected_month = request.GET.get("month")  # Get month filter from request

    data = defaultdict(lambda: {"orders": 0, "dispatches": 0, "received": 0})

    # Filter records by selected month (if provided) or fetch all
    orders = Order.objects.all()
    dispatches = Dispatch.objects.all()
    receiveds = Received.objects.all()

    if selected_month:
        orders = orders.filter(order_date_time__startswith=selected_month)
        dispatches = dispatches.filter(dispatch_date_time__startswith=selected_month)
        receiveds = receiveds.filter(received_date_time__startswith=selected_month)

    for order in orders:
        month = order.order_date_time.strftime("%Y-%m")
        data[month]["orders"] += 1

    for dispatch in dispatches:
        month = dispatch.dispatch_date_time.strftime("%Y-%m")
        data[month]["dispatches"] += 1

    for received in receiveds:
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