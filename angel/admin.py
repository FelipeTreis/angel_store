from django.contrib import admin

from angel.models import Category, Clothes


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'id', 'title', 'category', 'created_at')
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'category', 'gender', 'description',)
    list_filter = ('category', 'is_published', 'gender', 'created_at')
    list_per_page = 10
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ('title',)}
    autocomplete_fields = 'brands',


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category',)


admin.site.register(Category, CategoryAdmin)
