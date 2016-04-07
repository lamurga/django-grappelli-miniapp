from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('alpacuna.urls.site')),
)
