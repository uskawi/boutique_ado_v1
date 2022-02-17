from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Products list display """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'description',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Ctegories display"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
