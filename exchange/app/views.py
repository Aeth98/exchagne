from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import Register
from .forms import PlaceOrder
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Profile
from .models import Order

def register_page(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            user_profile = Profile.objects.create(user=user, balance=10, available_balance=10, total_profit_loss=0)
            user_profile.save()
            messages.success(request, 'Account successfully created.')
            return redirect('loginpage')
    else:
        form = Register()
    return render(request, 'app/registerpage.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'app/loginpage.html', {})

def home_page(request):
    if not request.user.is_authenticated:
        return render(request, 'app/loginpage.html')
    return render(request, 'app/homepage.html', {})

def place_order(request):
    if not request.user.is_authenticated:
        return render(request, 'app/loginpage.html')
    if request.method == 'POST':
        form = PlaceOrder(request.POST)
        if form.is_valid():
            form.save()
            type = request.POST.get('type')
            order = Order.objects.last()
            quantity = order.quantity
            order.quantity_tbf = quantity
            order.type = type
            order.profit_loss = 0
            price = order.price
            user_profile = Profile.objects.get(user=request.user)
            order.profile = user_profile

            if order.type == 'sell':
                if quantity <= user_profile.available_balance:
                    user_profile.available_balance = user_profile.available_balance - quantity
                    order.save()
                    user_profile.save()
                    messages.info(request, "Order placed.")
                else:
                    order.delete()
                    messages.info(request, "You don't have enough balance to sell.")

            if order.type == 'buy':
                matched_orders = Order.objects.filter(type='sell', price__lte=price, status='active')
                if len(matched_orders) > 0:
                    for matched_order in matched_orders:
                        matched_profile = matched_order.profile
                        quantity_tbf = order.quantity_tbf
                        quantity_to_swap = matched_order.quantity_tbf
                        order.quantity_tbf = order.quantity_tbf - matched_order.quantity_tbf
                        matched_order.quantity_tbf = matched_order.quantity_tbf - quantity_tbf
                        if order.quantity_tbf <= 0:
                            order.status = 'filled'
                            order.quantity_tbf = 0
                            quantity_to_swap = quantity_tbf
                            messages.info(request, "Order completely filled.")
                        else:
                            messages.info(request, "Order partially filled.")
                        if matched_order.quantity_tbf <= 0:
                            matched_order.status = 'filled'
                            matched_order.quantity_tbf = 0

                        order.profit_loss = order.profit_loss - quantity_to_swap * price
                        matched_order.profit_loss = matched_order.profit_loss + quantity_to_swap * price
                        user_profile.total_profit_loss = user_profile.total_profit_loss - quantity_to_swap * price
                        matched_profile.total_profit_loss = matched_profile.total_profit_loss + quantity_to_swap * price

                        user_profile.balance = user_profile.balance + quantity_to_swap
                        user_profile.available_balance = user_profile.available_balance + quantity_to_swap
                        matched_profile.balance = matched_profile.balance - quantity_to_swap

                        order.save()
                        matched_order.save()
                        user_profile.save()
                        matched_profile.save()

                        if order.status == 'filled':
                            break
                messages.info(request, "Order placed.")
    form = PlaceOrder()
    user_profile = Profile.objects.get(user=request.user)
    user_balance = user_profile.balance
    user_available_balance = user_profile.available_balance
    return render(request, 'app/placeorder.html', {'form': form, 'user_available_balance': user_profile.available_balance, 'user_balance': user_profile.balance})

def history(request):
    user_profile = Profile.objects.get(user=request.user)
    my_orders = Order.objects.filter(profile=user_profile)
    return render(request, 'app/history.html', {'my_orders': my_orders, 'user_profile': user_profile})

def active_orders(request):
    active_orders_list = Order.objects.filter(status='active')
    return render(request, 'app/activeorders.html', {'active_orders_list': active_orders_list})

def logoutpage(request):
    logout(request)
    redirect('app/logoutpage.html')
    return render(request, 'app/logoutpage.html', {})