from django.views.generic import DetailView
from apps.pages.models import Page
from apps.products.models import Product


class PageDetailView(DetailView):
    template_name = 'pages/page.html'
    model = Page
    context_object_name = 'page'

    def get_object(self, queryset=None):
        r = self.model.objects.get(slug=self.kwargs['slug'], status=self.model.STATUS_ACTIVE)
        return r

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product
        return context