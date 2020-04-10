import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.authtoken.models import Token
from .EmailBackEnd import EmailBackEnd
from .decorator import CustomUserCheck, CustomAuthenticationBackend, login_credentials
from .models import*
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
import pprint
#json
from django.views.generic import View
from django.http import JsonResponse
#api
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from . models import RecommendationDish
from . serializer import RecommendationDishSerializer
# from django.contrib.auth import login as auth_login


# Create your views here.
def user_login(request):
    return render(request,'restro/login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/manager_home')
            elif user.user_type == "2":
                return HttpResponseRedirect('/order')
            elif user.user_type == "3":
                return HttpResponse("Waiter login" + str(user.user_type))
            elif user.user_type == "4":
                return HttpResponse("Chef login" + str(user.user_type))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User "+request.user.email+" usertype: "+request.user.user_type)
    else:
        return HttpResponse("Please login first")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


# @login_required(login_url='login')
class OrdersView(ListView):
    model = TableOrder
    template_name = 'restro/restro_order.html'

    # context_object_name = 'orders'
    def get_context_data(self, **kwargs):
        table_number=self.request.GET.get("table_numbers")
        data = super().get_context_data(**kwargs)
        data['table'] = TableNumber.objects.all()
        print(data['table'],'tables')
        data['beverageItem'] = BeverageItem.objects.all()
        data['dishItem'] = DishItem.objects.all()
        data['orders'] = TableOrder.objects.filter(table_number=table_number).order_by('-id')
        # data['orders']=TableOrder.objects.filter(item=table_number).order_by('-id')
        # print(data['orders'], 'i am here.')
        return data


class CreateOrdersView(View):
    def get(self, request):
        item1 = request.GET.get('item')
        qty1 = request.GET.get('qty', None)

        obj = TableOrder.objects.create(
            item=item1,
            qty=qty1
        )

        user = {'id': obj.id, 'item': obj.item, 'qty': obj.qty}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateOrdersView(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        sn1 = request.GET.get('sn', None)
        item1 = request.GET.get('item')
        qty1 = request.GET.get('qty', None)
        rate1 = request.GET.get('rate', None)
        total1 = request.GET.get('total', None)

        obj = TableOrder.objects.get(id=id1)
        obj.sn = sn1
        obj.item = item1
        obj.qty = qty1
        obj.rate = rate1
        obj.total = total1
        obj.save()

        user = {'id': obj.id, 'sn': obj.sn, 'item': obj.item, 'qty': obj.qty, 'rate': obj.rate, 'total': obj.total}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteOrdersView(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        TableOrder.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def beverage_list(request):
    beverageItem = BeverageItem.objects.all()
    return render(request, 'restro/beverage_list.html', {'beverageItem': beverageItem})


class RecommendationDishList(APIView):

    def get(self, request):
        recommendationDish1=RecommendationDish.objects.all()
        serializer= RecommendationDishSerializer(recommendationDish1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class AssignTableView(ListView):
    model = AssignTable
    template_name = 'restro/assign_table.html'
    context_object_name = 'users'


class CreateAssignTable(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        table1 = request.GET.get('table', None)

        obj = AssignTable.objects.create(
            name = name1,
            table = table1
        )

        user = {'id':obj.id,'name':obj.name,'table':obj.table}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateAssignTable(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        table1 = request.GET.get('table', None)

        obj = AssignTable.objects.get(id=id1)
        obj.name = name1
        obj.table = table1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'table':obj.table}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteAssignTable(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        AssignTable.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


# @login_required(login_url='login')
class ReservationView(ListView):
    model = ReservationTable
    template_name = 'restro/reservation_table.html'
    context_object_name = 'reserves'


class CreateReservation(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        number1 = request.GET.get('number', None)
        table1 = request.GET.get('table', None)
        reservation_date1 = request.GET.get('reservation_date', None)
        time_from1 = request.GET.get('time_from', None)
        time_to1 = request.GET.get('time_to', None)

        obj = ReservationTable.objects.create(
            name=name1,
            number=number1,
            table=table1,
            reservation_date=reservation_date1,
            time_from=time_from1,
            time_to=time_to1
        )

        user = {'id': obj.id, 'name': obj.name, 'number': obj.number, 'table': obj.table,
                'reservation_date': obj.reservation_date, 'time_from': obj.time_from, 'time_to': obj.time_to}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateReservation(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        number1 = request.GET.get('number', None)
        table1 = request.GET.get('table', None)
        reservation_date1 = request.GET.get('reservation_date', None)
        time_from1 = request.GET.get('time_from', None)
        time_to1 = request.GET.get('time_to', None)

        obj = ReservationTable.objects.get(id=id1)
        obj.name = name1
        obj.number = number1
        obj.table = table1
        obj.reservation_date = reservation_date1
        obj.time_from = time_from1
        obj.time_to = time_to1
        obj.save()

        user = {'id': obj.id, 'name': obj.name, 'number': obj.number, 'table': obj.table,
                'reservation_date': obj.reservation_date, 'time_from': obj.time_from, 'time_to1': obj.time_to}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteReservation(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        ReservationTable.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def placeOrder(request):

    if request.method == 'POST':
        table = request.POST['tableno']
        table1 = TableNumber.objects.get(id=table)
        dishes = request.POST.get('dishes', None)
        quantity = request.POST['quantity']

        if dishes:
            dishes1 = DishItem.objects.get(id=dishes)
            total = quantity * int(dishes1.price)
            print(total)
        else:
            dishes1 = None

        beverage = request.POST.get('beverage',None)
        if beverage:
            beverage1=BeverageItem.objects.get(id=beverage)
            print(quantity)
            print(beverage1.price)
            total = int(quantity)*int(beverage1.price)
            print(total)

        else:
            beverage1=None
        print(beverage1)
        order = TableOrder.objects.create(table_number=table1, quantity=quantity, beverage=beverage1, dishes=dishes1,
                                          total=total)
        return redirect(request.META.get('HTTP_REFERER'))


class WaiterChefLogin(generics.GenericAPIView):

    @login_credentials
    def post(self, request, data=None):
        token = ''
        user = ''
        try:
            email_or_phone = data.get('email_or_phone')
            password = data.get('password')

            # Check if waiter user or chef user exist or not.
            user_check = CustomUserCheck.check_user(email_or_phone)
            if not user_check:
                return JsonResponse({
                    'status': HTTP_400_BAD_REQUEST,
                    'message': 'Not such user exist.',
                })

            # checking there password.
            user = CustomAuthenticationBackend.authenticate(email_or_phone, password)
            if not user:
                return JsonResponse({
                    'status': HTTP_400_BAD_REQUEST,
                    'message': 'Invalid Credentials.',
                })

            # creating unique token for that user.
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({
                'status': HTTP_200_OK,
                'token': token.key,
                'message': 'Login Successfully',
            })

        except Exception as e:
            return JsonResponse({
                'status': HTTP_400_BAD_REQUEST,
                'message': 'Error: ' + str(e),
            })
