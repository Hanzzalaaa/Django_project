from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('crud/', include(router.urls)),
    path('customer_search/',Search.as_view(), name= 'customer_search'),
]