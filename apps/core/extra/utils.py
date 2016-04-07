from django.utils.text import slugify


def clean_slugify(val):
    if not isinstance(val, unicode):
        val = unicode(val)
    return slugify(val)