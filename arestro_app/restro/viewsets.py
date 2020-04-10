from rest_framework import viewsets
from . import models
from . import serializer
from .serializer import WaiterSerializer, ChefSerializer, TableOrderSerializer, TableNumberSerializer, NotificationSerializer, PackingRequestSerializer, PlaceOrderSerializer
# TableOrderSerializer


class WaiterViewset(viewsets.ModelViewSet):
    queryset = models.Waiter.objects.all()
    serializer_class = WaiterSerializer


class ChefViewset(viewsets.ModelViewSet):
    queryset = models.Chef.objects.all()
    serializer_class = ChefSerializer


class TableOrderViewset(viewsets.ModelViewSet):
    queryset = models.TableOrder.objects.all()
    serializer_class = TableOrderSerializer


class TableNumberViewset(viewsets.ModelViewSet):
    queryset = models.TableNumber.objects.all()
    serializer_class = TableNumberSerializer


class NotificationViewset(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = NotificationSerializer


class PackingRequestViewset(viewsets.ModelViewSet):
    queryset = models.PackingRequest.objects.all()
    serializer_class = PackingRequestSerializer


class PlaceOrderViewset(viewsets.ModelViewSet):
    queryset = models.PlaceOrder.objects.all()
    serializer_class = PlaceOrderSerializer