from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OrderForm, ItemForm, UpdateStatusOrderForm
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
    all_orders = Order.objects.all()
    return render(
        request,
        "orders.html",
        {
            'orders': all_orders,
            'revenue': sum(
                list(all_orders.filter(status='Оплачено')
                .values_list('total_price',flat=True))
            )
        }
    )

def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateStatusOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/orders/")
    else:
        form = UpdateStatusOrderForm(instance=order)
    return render(request, 'edit_order.html', {'form': form, 'order': order})

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect("/orders/")
    return render(request, 'delete_order.html', {'order': order})

def post_items(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/orders/")
    else:
        form = ItemForm()
    return render(request, "create_items.html", {"form": form})

def home(request):
    return render(request, "home.html")
