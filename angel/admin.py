from django.contrib import admin

from angel.models import Category, Clothes


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
