from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from .models import *

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

# Register your models here.
admin.site.register(BeverageCategorie)
admin.site.register(BeverageItem)
admin.site.register(DishCategorie)
admin.site.register(DishItem)
admin.site.register(RecommendationDish)
admin.site.register(TableNumber)
admin.site.register(ReservationTable)
admin.site.register(TableOrder)

admin.site.register(Notification)
admin.site.register(PackingRequest)
admin.site.register(PlaceOrder)