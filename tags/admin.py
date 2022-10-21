from django.contrib import admin

# Register your models here.
from tags.models import Tag, TaggedItem

admin.site.register(Tag)
admin.site.register(TaggedItem)


class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
