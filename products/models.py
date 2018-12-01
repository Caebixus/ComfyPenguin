from django.db import models

# Create your models here.

class ProductHoodies(models.Model):
    title = models.CharField(max_length=35)
    pub_date = models.DateTimeField()
    seller_choices = (('UK', 'Amazon.co.uk'), ('DE', 'Amazon.de'), ('US', 'Amazon.com'), ('AL', 'Aliexpress.com'))
    seller = models.CharField(max_length=2, choices=seller_choices, default='Amazon.co.uk')
    item_url = models.URLField()
    item_image = models.ImageField(height_field=30, width_field=10)

# ASIN
# Type of clothes
# width of clothes
# height of clothes


class ProductSweatshirts(models.Model):
    title = models.CharField(max_length=35)
    pub_date = models.DateTimeField()
    seller_choices = (('UK', 'Amazon.co.uk'), ('DE', 'Amazon.de'), ('US', 'Amazon.com'), ('AL', 'Aliexpress.com'))
    seller = models.CharField(max_length=2, choices=seller_choices, default='Amazon.co.uk')
    item_url = models.URLField()
    item_image = models.ImageField(height_field=30, width_field=10)
