from django.db import models


STATUS_CHOICES = [
    ('In waiting', 'В ожидании'),
    ('Ready', 'Готово'),
    ('Paid', 'Оплачено')
]

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.JSONField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.table_number)

    def save(self, *args, **kwargs):
        self.total_price = sum(item.get('price', 0.00) for item in self.items)
        super().save(*args, **kwargs)
