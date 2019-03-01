from django.contrib import admin

# Register your models here.

from .models import Product_Clothes

class PostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('item_title', 'item_size', 'item_category','item_color', 'item_asin', 'item_url', 'upload_date')
    list_filter = ('item_category', 'item_gender', 'item_seller')
    search_fields = ('item_title', 'item_asin')

admin.site.register(Product_Clothes, PostAdmin)
