from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# created in a tuple set of Manager, Cashier, Waiter and Chef
class CustomUser(AbstractUser):
	user_type_data = ((1, "Manage"), (2, "Cashier"), (3, "Waiter"), (4, "Chef"))
	user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Manage(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class Cashiers(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class Waiter(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class Chef(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()


class BeverageCategorie(models.Model):
	name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class BeverageItem(models.Model):
	beverage = models.ForeignKey(BeverageCategorie, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(max_length=200, null=True)
	quantity = models.CharField(max_length=100, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class DishCategorie(models.Model):
	name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class DishItem(models.Model):
	beverage = models.ForeignKey(DishCategorie, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(max_length=200, null=True)
	quantity = models.CharField(max_length=100, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class TableNumber(models.Model):
	tableName = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.tableName


class Notification(models.Model):
	notify = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.notify


class PackingRequest(models.Model):
	req = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.req


class PlaceOrder(models.Model):
	table_number = models.ForeignKey(TableNumber, null=True, on_delete=models.SET_NULL)
	beverage = models.ForeignKey(BeverageItem, null=True, on_delete=models.SET_NULL)
	dishes = models.ForeignKey(DishItem, null=True, blank=True, on_delete=models.SET_NULL)
	total = models.CharField(max_length=100, blank=True)
	quantity=models.IntegerField()

	def __str__(self):
		return self.req


class AssignTable(models.Model):
	name = models.CharField(max_length=30, blank=True)
	table = models.CharField(max_length=100, blank=True)


class TableOrder(models.Model):
	table_number = models.ForeignKey(TableNumber, null=True, on_delete=models.SET_NULL)
	beverage = models.ForeignKey(BeverageItem, null=True, on_delete=models.SET_NULL)
	rate = models.CharField(max_length=100, blank=True)
	dishes = models.ForeignKey(DishItem, null=True, blank=True, on_delete=models.SET_NULL)
	quantity = models.CharField(max_length=100, null=True)
	total = models.CharField(max_length=100, blank=True)
	quantity = models.IntegerField()

	def __str__(self):
		return self.table_number.tableName


class RecommendationDish(models.Model):
	sn = models.CharField(max_length=200, null=True)
	dishes = models.ForeignKey(DishItem, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.sn


class ReservationTable(models.Model):
	name = models.CharField(max_length=100, null=True)
	number = models.CharField(max_length=100, null=True)
	table = models.CharField(max_length=100, null=True)
	reservation_date = models.CharField(max_length=100, null=True)
	time_from = models.CharField(max_length=100, null=True)
	time_to = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		if instance.user_type == 1:
			Manage.objects.create(admin=instance)

		if instance.user_type == 2:
			Cashiers.objects.create(admin=instance)

		if instance.user_type == 3:
			Waiter.objects.create(admin=instance)

		if instance.user_type == 4:
			Chef.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	if instance.user_type == 1:
		instance.manage.save()

	if instance.user_type == 2:
		instance.cashiers.save()

	if instance.user_type == 3:
		instance.waiter.save()

	if instance.user_type == 4:
		instance.chef.save()