from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("product__price") * F("quantity"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']


class OrderLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} de {self.product.name}'

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedidos'
        ordering = ['id']
