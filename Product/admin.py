from django.contrib import admin
from .models import Category, Product, Brand



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'store', 'is_product_available', 'created_at', 'updated_at','was_published_recently']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price', 'store']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
