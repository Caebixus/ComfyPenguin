from django.db import models
from datetime import datetime

# Create your models here.

class Product_Clothes(models.Model):
    item_title = models.CharField(max_length=35, null = True)

    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unisex', 'Unisex'),
    )
    item_gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null = True)

    CATEGORY_CHOICES = (
    ('Sweatshirt', 'Sweatshirt'),
    ('Hoodies', 'Hoodies'),
    ('Jumper', 'Jumper'),
    )
    item_category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, null = True)

    item_asin = models.CharField(max_length=40, null = True)

    item_price = models.DecimalField(help_text='Price of product even with decimals', max_digits=10, decimal_places=2, null = True)

    CURRENCY_CHOICES = (
    ('EUR', 'EUR'),
    ('GPB', 'GPB'),
    ('USD', 'USD'),
    )
    item_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null = True)

    item_width = models.IntegerField(default=52, help_text='Use width in centimeters', null = True)
    item_height = models.IntegerField(default=72, help_text='Use height in centimeters', null = True)

    item_url = models.URLField(help_text='To add size to link on Amazon - use Short links', max_length=150, null = True)

    image_main = models.ImageField(max_length=200, upload_to='images/', null = True)
    image_secondary = models.ImageField(max_length=200, upload_to='images/', null = True, blank = True)
    image_third = models.ImageField(max_length=200, upload_to='images/', null = True, blank = True)

    upload_date = models.DateTimeField(default=datetime.now, null = True)

    def __str__(self):
        return self.item_title