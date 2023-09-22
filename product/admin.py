from django.contrib import admin

from .models import City, District, Ban, Banflud, Category, Product

admin.site.register(City)
admin.site.register(District)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'description', 'price', 'is_active', 'is_banned', 'updated_at', 'is_deleted']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'is_banned', 'is_deleted']


@admin.register(Banflud)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Ban)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['comment', 'banflud', 'product', 'user']
