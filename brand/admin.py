from django.contrib import admin

from brand.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = 'brand',
    list_display_links = 'brand',
    search_fields = 'brand',
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('brand', ),
    }
