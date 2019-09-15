from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Product_Clothes_Tops, Product_Clothes_Tops_US, ProductClothesTopsProxy, ProductClothesTopsUSProxy

class PostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('item_title', 'item_size', 'item_category','item_color', 'item_url', 'item_continent', 'item_width', 'item_height', 'upload_date')
    list_filter = ('item_category', 'item_gender', 'item_seller', 'item_continent')
    search_fields = ('item_title', 'item_asin', 'item_brand')

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product_Clothes_Tops

class ProductExportAdmin(ImportExportModelAdmin):
    resource_class = ProductResource

admin.site.register(Product_Clothes_Tops, PostAdmin)
admin.site.register(Product_Clothes_Tops_US, PostAdmin)

admin.site.register(ProductClothesTopsProxy, ProductExportAdmin)
admin.site.register(ProductClothesTopsUSProxy, ProductExportAdmin)
