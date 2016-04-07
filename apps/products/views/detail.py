# coding=utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, CreateView
from apps.products.forms.Order import OrderForm
from apps.products.models import Product, Order


class ProductDetailView(DetailView):
    template_name = "products/detail.html"
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'], category__slug=self.kwargs['category'],
                                         status=self.model.STATUS_ACTIVE)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product
        return context


class OrderFormView(CreateView):
    template_name = 'products/order.html'
    model = Order
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = self.get_object()
            return self.form_valid(form)
        else:
            self.object = None
            return self.form_invalid(form)

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['slug'], status=Product.STATUS_ACTIVE)

    def get_success_url(self):
        messages.success(self.request,
                         u'Solicitud envíada con éxito. Pronto nos pondremos en contacto con usted. Gracias!')
        return reverse_lazy('order_detail_product', args=[self.kwargs['category'], self.kwargs['slug']])

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)

        context['product'] = self.get_object()
        context['category_product'] = Product.list_category_product
        return context