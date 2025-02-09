from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, DispatchViewSet, ReceivedViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'dispatches', DispatchViewSet)
router.register(r'received', ReceivedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
