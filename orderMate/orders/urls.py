from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, DispatchViewSet, ReceivedViewSet
from .views import monthly_summary
from .views import monthly_summary_page

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'dispatches', DispatchViewSet)
router.register(r'received', ReceivedViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('summary-page/', monthly_summary_page, name='monthly-summary-page'),
    path('summary/', monthly_summary, name='monthly-summary'),
]
