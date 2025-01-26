from django import forms
from .models import Item, Order


ITEMS_CHOICES= [tuple([int(x.id), x.name]) for x in Item.objects.all()]


class OrderForm(forms.ModelForm):
    all_items = forms.CharField(label="Выберите блюда", widget=forms.SelectMultiple( choices=ITEMS_CHOICES))

    class Meta:
        model = Order
        fields = ('table_number',)
        labels = {
            'table_number': 'Номер стола',
        }