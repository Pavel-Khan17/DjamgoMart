from django.contrib import admin
from . models import ProductModel
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
   prepopulated_fields= {'slug' : ('product_name',)}
   list_display=('product_name', 'slug', 'price', 'stock','created_date', 'modified_date','is_available')

admin.site.register(ProductModel,ProductAdmin)