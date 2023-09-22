from django.contrib import admin

from .models import City, District

admin.site.register(City)
admin.site.register(District)

from account.models import CustomUser
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'description', 'price', 'is_active', 'is_banned', 'updated_at', 'is_deleted']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'is_banned', 'is_deleted']

admin.site.register(Product, ProductAdmin)
