# coding=utf-8
from django.db import models
from apps.categories.models import CategorySubCategory, Category
from apps.core.extra.SlugifyUniquely import SlugifyUniquely


class Product(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    STATUS_CHOICES = (
        (STATUS_ACTIVE, u'Activo'),
        (STATUS_INACTIVE, u'Inactivo')
    )

    CURRENCY_USD = 3  # EEUU
    CURRENCY_PEN = 2  # PERU
    CURRENCY_CHF = 1  # SUIZA

    CURRENCIES = (
        (CURRENCY_CHF, u'CHF'),
        (CURRENCY_PEN, u'PEN'),
        (CURRENCY_USD, u'USD'),
    )

    category = models.ForeignKey(
        Category,
        related_name='product_category_set',
        verbose_name=u'Categoría'
    )

    subcategory = models.ForeignKey(
        CategorySubCategory,
        null=True,
        editable=False,
        related_name='sub_category_set',
        verbose_name=u'SubCategoría'
    )
    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    slug = models.SlugField(editable=False, max_length=150, null=True, default=None)
    description = models.TextField(
        null=True,
        verbose_name=u'Descripción'
    )
    details = models.TextField(
        null=True,
        verbose_name=u'Detalle'
    )
    informations = models.TextField(
        null=True,
        verbose_name=u'Información General'
    )
    currency = models.SmallIntegerField(
        choices=CURRENCIES,
        null=True,
        verbose_name=u'Moneda'
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        verbose_name=u'Precio'
    )
    photo = models.ImageField(upload_to='media/', blank=True, verbose_name=u'Foto')
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        verbose_name=u'Creado en'
    )
    updated_at = models.DateTimeField(
        editable=False,
        auto_now=True,
        verbose_name=u'Actualizado en'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        verbose_name=u'Estado'
    )

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if self.slug is None:
            self.slug = SlugifyUniquely(self.name, self.__class__)

        super(Product, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Lista de Productos"
        app_label = 'products'


    @classmethod
    def list_category_product(cls):
        result = cls.objects.filter(status=cls.STATUS_ACTIVE).values('category__name',
                                                                     'category__slug',
                                                                     'name',
                                                                     'slug',
                                                                     'description').order_by('category__name')
        return result

    @classmethod
    def list_product(cls):
        result = cls.objects.filter(status=cls.STATUS_ACTIVE)
        result = result.order_by('-id')[0:3]
        return result