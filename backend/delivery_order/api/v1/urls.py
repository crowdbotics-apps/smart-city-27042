from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet, BillViewSet, PaymentMethodViewSet

router = DefaultRouter()
router.register("bill", BillViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("order", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
