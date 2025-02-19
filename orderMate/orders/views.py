import json
from collections import defaultdict
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from orders.models import Order, Dispatch, Received
from orders.serializers import OrderSerializer, DispatchSerializer, ReceivedSerializer

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
    Returns a JSON summary of orders, dispatches, and received records per month.
    If a specific month (YYYY-MM) is provided as a query parameter, filters results accordingly.
    """
    selected_month = request.GET.get("month")  # Example: "2025-02"
    data = defaultdict(lambda: {"orders": 0, "dispatches": 0, "received": 0})

    # Fetch all records initially
    orders = Order.objects.all()
    dispatches = Dispatch.objects.all()
    receiveds = Received.objects.all()

    # Debugging logs
    print(f"Selected Month: {selected_month}")

    # If a month is selected, filter data accordingly
    if selected_month:
        try:
            year, month = map(int, selected_month.split('-'))
            orders = orders.filter(order_date_time__year=year, order_date_time__month=month)
            dispatches = dispatches.filter(dispatch_date_time__year=year, dispatch_date_time__month=month)
            receiveds = receiveds.filter(received_date_time__year=year, received_date_time__month=month)
        except ValueError:
            return JsonResponse({"error": "Invalid date format. Use YYYY-MM"}, status=400)

    # Check if data exists before processing
    if not orders.exists() and not dispatches.exists() and not receiveds.exists():
        return JsonResponse({"error": "No records found for the selected month"}, status=200)

    # Populate data dictionary
    for order in orders:
        month_str = order.order_date_time.strftime("%Y-%m")
        data[month_str]["orders"] += 1

    for dispatch in dispatches:
        month_str = dispatch.dispatch_date_time.strftime("%Y-%m")
        data[month_str]["dispatches"] += 1

    for received in receiveds:
        month_str = received.received_date_time.strftime("%Y-%m")
        data[month_str]["received"] += 1

    # Debugging: Print fetched data
    print("Summary Data:", dict(data))

    return JsonResponse(dict(data))

# HTML Page for Monthly Summary
def monthly_summary_page(request):
    """
    Renders the monthly summary page.
    """
    try:
        # Fetch data using API to ensure correct format
        response = monthly_summary(request)
        data = json.loads(response.content.decode('utf-8'))

        # Debugging: Print fetched data for verification
        print("Page Data:", data)

        return render(request, "orders/summary.html", {"data": data})
    
    except Exception as e:
        return render(request, "orders/summary.html", {"data": {}, "error": str(e)})
