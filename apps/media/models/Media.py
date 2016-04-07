# coding=utf-8
from django.db import models


class Photo(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    STATUS_CHOICES = (
        (STATUS_ACTIVE, u'Activo'),
        (STATUS_INACTIVE, u'Inactivo')
    )

    SHOW_HOME = 1
    SHOW_GALERY = 0

    SHOW_CHOICES = (
        (SHOW_GALERY, u'Galería'),
        (SHOW_HOME, u'Página Inicio')
    )

    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    file = models.ImageField(upload_to='media/photo/', blank=True, verbose_name=u'Foto')
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        editable=False,
        auto_now=True,
        verbose_name=u'Fecha Actualización'
    )
    show_at = models.SmallIntegerField(
        choices=SHOW_CHOICES,
        default=SHOW_GALERY,
        verbose_name=u'Mostrar en'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        verbose_name=u'Estado'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Foto"
        verbose_name_plural = u"Lista de Fotos"
        app_label = 'media'


class Video(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    STATUS_CHOICES = (
        (STATUS_ACTIVE, u'Activo'),
        (STATUS_INACTIVE, u'Inactivo')
    )

    name = models.CharField(max_length=100, verbose_name=u'Nombre')
    url = models.URLField(verbose_name=u'URL Video')
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        editable=False,
        auto_now=True,
        verbose_name=u'Fecha Actualización'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        verbose_name=u'Estado'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Video"
        verbose_name_plural = u"Lista de Videos"
        app_label = 'media'