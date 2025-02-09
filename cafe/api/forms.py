from django import forms
from .models import Item, Order



class OrderForm(forms.ModelForm):
    all_items = forms.ModelMultipleChoiceField(label="Выберите блюда", queryset=Item.objects.all())
    class Meta:
        model = Order
        fields = ('table_number',)
        labels = {
            'table_number': 'Номер стола',
        }

class UpdateStatusOrderForm(forms.ModelForm):
    all_items = forms.ModelMultipleChoiceField(label="Выберите блюда", queryset=Item.objects.all())
    class Meta:
        model = Order
        fields = ('status', )
        labels = {
            'status': 'Статус заказа',
        }
    def __init__(self, *args, **kwargs):
        super(UpdateStatusOrderForm, self).__init__(*args, **kwargs)
        self.fields['all_items'].required = False


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'Название блюда',
            'price': 'Цена блюда'
        }