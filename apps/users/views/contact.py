# coding=utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from apps.products.models import Product
from apps.users.forms.Contact import ContactForm


class ContactFormView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactForm

    def get_success_url(self):
        messages.success(self.request,
                         u'Datos envíados con éxito. Pronto nos pondremos en contacto con usted. Gracias!')
        return reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)

        context['category_product'] = Product.list_category_product
        return context