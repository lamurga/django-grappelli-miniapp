# coding=utf-8
from django.db import models
from apps.core.extra.SlugifyUniquely import SlugifyUniquely


class Page(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    STATUS_CHOICES = (
        (STATUS_ACTIVE, u'Activo'),
        (STATUS_INACTIVE, u'Inactivo')
    )

    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    slug = models.SlugField(editable=False, max_length=150, null=True, default=None)
    description = models.TextField(
        null=True,
        verbose_name=u'Descripción'
    )
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

        super(Page, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Páginas"
        verbose_name_plural = "Lista de Páginas"
        app_label = 'pages'