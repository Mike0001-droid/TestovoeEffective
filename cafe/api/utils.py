from .models import Item
from django import forms
import ast


def get_items_from_form(form: forms.ModelForm) -> None:
    obj = form.save(commit=False)
    items_ids = ast.literal_eval(form.cleaned_data['all_items'])
    items = list(Item.objects.filter(id__in=items_ids).values('price', 'name'))
    obj.items = items
    obj.total_price = sum(item['price'] for item in items)
    obj.save()
    return None