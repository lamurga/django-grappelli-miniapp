from django.contrib import admin
from apps.pages.models import Page
from apps.products.models import Product, Order
from apps.categories.models import CategorySubCategory, Category
from apps.media.models import Photo, Video
from apps.users.models import Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')


class MediaPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_at', 'updated_at')


class MediaVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'updated_at')


class CategorySubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'contact_name', 'contact_email', 'contact_phone', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'updated_at', 'status')

    class Media:
        def __init__(self):
            pass

        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'status')

    class Media:
        def __init__(self):
            pass

        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]

admin.site.register(Contact)
admin.site.register(Photo, MediaPhotoAdmin)
admin.site.register(Video, MediaVideoAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# admin.site.register(CategorySubCategory, CategorySubCategoryAdmin)