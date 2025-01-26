from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OrderForm
from .models import Order
from .utils import get_items_from_form


def post_orders(request):  
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            get_items_from_form(form)
            return HttpResponseRedirect("/orders/")
    else:
        form = OrderForm()
    return render(request, "create_orders.html", {"form": form})

def orders(request):
    return render(request, "orders.html", {'orders': Order.objects.all()})

def home(request):
    return render(request, "home.html")
