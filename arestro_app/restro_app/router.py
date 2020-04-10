from arestro_app.restro.viewsets import WaiterViewset, ChefViewset, TableOrderViewset, TableNumberViewset, NotificationViewset, PackingRequestViewset, PlaceOrderViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Waiter', WaiterViewset)
router.register('Chef', ChefViewset)
router.register('TakeOrder', TableOrderViewset)
router.register('TableNumber', TableNumberViewset)
router.register('PackingRequest', NotificationViewset)
router.register('TableNumber', PackingRequestViewset)
router.register('PlaceOrder', PlaceOrderViewset)
urlpatterns = router.urls
