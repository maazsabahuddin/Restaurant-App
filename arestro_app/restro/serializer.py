from rest_framework import serializers
from .models import Waiter, Chef, RecommendationDish, TableOrder, TableNumber, Notification, PackingRequest, PlaceOrder


class WaiterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Waiter
		fields = '__all__'


class ChefSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chef
		fields = '__all__'


class RecommendationDishSerializer(serializers.ModelSerializer):
	class Meta:
		model = RecommendationDish
		fields = '__all__'


class TableOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = TableOrder
		fields = '__all__'


class TableNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = TableNumber
		fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = '__all__'


class PackingRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = PackingRequest
		fields = '__all__'


class PlaceOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlaceOrder
		fields = '__all__'