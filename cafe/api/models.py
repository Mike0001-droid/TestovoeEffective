from django.db import models


STATUS_CHOICES = [
    ('In waiting', 'В ожидании'),
    ('Ready', 'Готово'),
    ('Paid', 'Оплачено')
]

class Item(models.Model):
    name = models.CharField("Название блюда", max_length=255)
    price = models.IntegerField("Цена за блюдо")

    def __str__(self):
        return f"Блюдо - {self.name}"


class Order(models.Model):
    table_number = models.IntegerField()
    total_price = models.IntegerField("Финальная стоимость")
    items = models.JSONField("Все блюда")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='В ожидании')

    def __str__(self):
        return str(self.table_number)
