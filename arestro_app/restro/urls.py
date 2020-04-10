from django.urls import path
from . import views, manageView
from django.conf.urls import include

urlpatterns = [
	path('add_cashier', manageView.add_cashier),
	path('add_cashier_save', manageView.add_cashier_save),
	path('add_chef', manageView.add_chef),
	path('add_chef_save', manageView.add_chef_save),
	path('add_waiter', manageView.add_waiter),
	path('add_waiter_save', manageView.add_waiter_save),
	path('', views.user_login, name="home"),
	path('get_user_details/', views.GetUserDetails),
	path('logout_user/', views.logout_user),
	path('doLogin/', views.doLogin),
	path('assign_table/',  views.AssignTableView.as_view(), name='assign_table'),
	path('ajax/assign_table/create/',  views.CreateAssignTable.as_view(), name='assign_table_ajax_create'),
	path('ajax/assign_table/update/',  views.UpdateAssignTable.as_view(), name='assign_table_ajax_update'),
	path('ajax/assign_table/delete/',  views.DeleteAssignTable.as_view(), name='assign_table_ajax_delete'),
	path('order/', views.OrdersView.as_view(), name='order_ajax'),
	path('placeorder/', views.placeOrder,name='placeorder'),
	path('ajax/crud/create/', views.CreateOrdersView.as_view(), name='crud_order_create'),
	path('ajax/crud/update/',  views.UpdateOrdersView.as_view(), name='crud_order_update'),
	path('ajax/crud/delete/',  views.DeleteOrdersView.as_view(), name='crud_order_delete'),
	path('manager_home', manageView.manager_home),
	path('reservation',  views.ReservationView.as_view(), name='reservation_ajax'),
	path('ajax/reservation_table/create/',  views.CreateReservation.as_view(), name='reservation_ajax_create'),
	path('ajax/reservation_table/update/', views.UpdateReservation.as_view(), name='reservation_ajax_update'),
	path('ajax/reservation_table/delete/', views.DeleteReservation.as_view(), name='reservation_ajax_delete'),
]