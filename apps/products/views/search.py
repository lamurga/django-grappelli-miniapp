from django.http import Http404
from django.views.generic import ListView
from apps.categories.models import Category
from apps.products.models import Product


class SearchListView(ListView):
    template_name = "products/search.html"
    model = Product
    context_object_name = 'products'

    def __init__(self, **kwargs):
        self.slug_category = None
        self.object_list = None
        self.category = None

        super(SearchListView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.slug_category = self.kwargs.get('category', None)

        allow_empty = self.get_allow_empty()
        if not allow_empty:
            raise Http404(u"Lista vacia")

        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)

        return self.render_to_response(context)

    def get_queryset(self):
        queryset = self.model.objects.filter(category__slug=self.slug_category, status=self.model.STATUS_ACTIVE)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product
        context['category'] = self.category

        return context

    def get_allow_empty(self):
        self.category = Category.objects.get(slug=self.slug_category)
        if self.slug_category:
            if not self.category:
                self.allow_empty = False

        return self.allow_empty