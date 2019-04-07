from django.contrib import admin

# Register your models here.

from .models import Product_Clothes_Tops

class PostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('item_title', 'item_size', 'item_category','item_color', 'item_asin', 'item_url', 'upload_date', 'item_continent')
    list_filter = ('item_category', 'item_gender', 'item_seller', 'item_continent')
    search_fields = ('item_title', 'item_asin', 'item_brand')

admin.site.register(Product_Clothes_Tops, PostAdmin)
