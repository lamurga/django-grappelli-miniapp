from django.db import models
from apps.products.models import Product


class Order(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='product_set',
        verbose_name=u'Producto'
    )
    quantity = models.IntegerField(max_length=10, verbose_name=u'Cantidad')
    contact_name = models.CharField(max_length=100, verbose_name=u'Nombre Contacto')
    contact_email = models.CharField(max_length=100, verbose_name=u'Email Contacto')
    contact_phone = models.CharField(max_length=50, verbose_name=u'Email Contacto')
    contact_message = models.TextField(null=True, verbose_name=u'Comentarios')
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Pedido"
        verbose_name_plural = u"Lista de Pedidos"
        app_label = 'products'