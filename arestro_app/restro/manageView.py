from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import CustomUser, Cashiers


def manager_home(request):
    return render(request, "restro/manager_home.html")


def add_cashier(request):
    return render(request,"restro/add_cashier.html")


def add_cashier_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.save()
            messages.success(request, "Successfully Added Cashier")
            return HttpResponseRedirect("/add_cashier")

        except:
            messages.error(request, "Failed to Add Cashier")
            return HttpResponseRedirect("/add_cashier")


def add_waiter(request):
    return render(request, "restro/add_waiter.html")


def add_waiter_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                                  first_name=first_name, user_type=3)
            user.save()
            messages.success(request, "Successfully Added Waiter")
            return HttpResponseRedirect("/add_waiter")
        except:
            messages.error(request, "Failed to Add Waiterr")
            return HttpResponseRedirect("/add_waiter")


def add_chef(request):
    return render(request, "restro/add_chef.html")


def add_chef_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                                  first_name=first_name, user_type=4)
            user.save()
            messages.success(request, "Successfully Added Chef")
            return HttpResponseRedirect("/add_chef")
        except:
            messages.error(request, "Failed to Add Chef")
            return HttpResponseRedirect("/add_chef")