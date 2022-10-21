from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem


# class TagInline(GenericTabularInline):
#     search_fields = ['tag']
#     model = TaggedItem
#
#
# class CustomProductAdmin(ProductAdmin):
#     search_fields = ['tag']
#     inlines = [TagInline]


admin.site.unregister(Product)
# admin.site.register(Product)
