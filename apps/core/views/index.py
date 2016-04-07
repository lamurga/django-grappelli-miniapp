# coding=utf-8
from django.views.generic import TemplateView, ListView
from apps.media.models import Photo, Video
from apps.products.models import Product


class HomeTemplateView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)

        context['photos'] = Photo.objects.filter(status=Photo.STATUS_ACTIVE, show_at=Photo.SHOW_HOME)
        context['category_product'] = Product.list_category_product
        context['shopping'] = Product.list_product

        return context


class VideoTemplateView(ListView):
    template_name = "pages/video.html"
    model = Video
    context_object_name = 'videos'

    def get_queryset(self):
        queryset = self.model.objects.filter(status=Video.STATUS_ACTIVE)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(VideoTemplateView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product

        return context


class PhotoTemplateView(ListView):
    template_name = "pages/photo.html"
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        queryset = self.model.objects.filter(status=Photo.STATUS_ACTIVE, show_at=Photo.SHOW_GALERY)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotoTemplateView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product

        return context