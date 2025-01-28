from .models import Item
from django import forms
from django.core import serializers
from json import dumps, loads

def get_items_from_form(form: forms.ModelForm) -> None:
    """
        Получает на вход форму создания заказа,
        сериализует Queryset в JSON, достает
        необходимые поля, просчитывает итоговую
        стоимость заказа и сохраняет даныне в базу
    """
    obj = form.save(commit=False)
    items_qs = (form.cleaned_data['all_items'])
    items_json = serializers.serialize("json", items_qs)
    items = [item['fields'] for item in loads(items_json)]
    obj.items = items
    obj.total_price = sum(item['price'] for item in items)
    obj.save()
    return None