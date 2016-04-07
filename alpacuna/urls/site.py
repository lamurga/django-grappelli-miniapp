from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from apps.core.views.index import HomeTemplateView, VideoTemplateView, PhotoTemplateView
from apps.pages.views.page import PageDetailView
from apps.products.views.detail import ProductDetailView, OrderFormView
from apps.products.views.search import SearchListView
from apps.users.views.contact import ContactFormView

urlpatterns = patterns('',
                       url(r'^$', HomeTemplateView.as_view(), name='home'),
                       url(r'^contacto$', ContactFormView.as_view(), name='contact'),
                       url(r'^videos$', VideoTemplateView.as_view(), name='video'),
                       url(r'^fotos', PhotoTemplateView.as_view(), name='photo'),
                       url(r'^p/(?P<slug>[\w-]+)', PageDetailView.as_view(), name='page'),
                       url(r'^(?P<category>[\w-]+)$', SearchListView.as_view(), name='search_category'),
                       url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)$', ProductDetailView.as_view(),
                           name='detail_product'),
                       url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/pedido$', OrderFormView.as_view(),
                           name='order_detail_product'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()