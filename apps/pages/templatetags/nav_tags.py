from django import template
from apps.pages.models import Page

register = template.Library()

@register.inclusion_tag('include/nav_page.html')
def get_pages():
    pages = Page.objects.filter(status=Page.STATUS_ACTIVE).values('name', 'slug')
    return {'pages': pages}