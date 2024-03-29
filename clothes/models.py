from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Amazon.de Model -----------------------------------------------------------------------------------------------------------------------------

class Product_Clothes_Tops(models.Model):
    item_brand = models.CharField(max_length=35, null = True)
    item_title = models.CharField(max_length=35, null = True)
    item_material_composition = models.CharField(max_length=80, blank=True, null = True, default="No information")
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unisex', 'Unisex'),
    ('Kids', 'Kids'),
    )
    item_gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null = True)
    CATEGORY_CHOICES = (
    ('Sweatshirt', 'Sweatshirt'),
    ('Hoodies', 'Hoodies'),
    ('Jumper', 'Jumper'),
    ('Jacket', 'Jacket'),
    ('Cardigan', 'Cardigan'),
    ('Short', 'Short'),
    )

    item_category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, null = True)
    item_asin = models.CharField(max_length=40, null = True)
    item_size = models.CharField(max_length=4, null = True)
    item_price = models.DecimalField(help_text='Price of product even with decimals', max_digits=10, decimal_places=2, null = True)
    CURRENCY_CHOICES = (
    ('EUR', 'EUR'),
    ('GPB', 'GPB'),
    ('USD', 'USD'),
    )
    item_color = models.CharField(max_length=60, null = True)
    item_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null = True, default="EUR")
    item_width = models.FloatField(default=52, help_text='Use width in centimeters', null = True)
    item_height = models.FloatField(default=72, help_text='Use height in centimeters', null = True)
    item_url = models.URLField(help_text='To add size to link on Amazon - use Short links', max_length=500, null = True)
    item_seller = models.CharField(max_length=25, null = True, default="Amazon")
    image_main = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True)
    image_secondary = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True, blank = True)
    image_third = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True, blank = True)
    CONTINENT_CHOICES = (
    ('Europe', 'Europe'),
    ('North America', 'North America'),
    ('South America', 'South America'),
    ('Asia', 'Asia'),
    ('Africa', 'Africa'),
    ('Australia', 'Australia'),
    ('Worldwide', 'Worldwide'),
    )
    item_continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES, null = True, default="Europe")
    upload_date = models.DateTimeField(default=datetime.now, null = True)

    def __str__(self):
        return self.item_title

class ProductClothesTopsProxy(Product_Clothes_Tops):
    class Meta:
        proxy = True


# USA Model -----------------------------------------------------------------------------------------------------------------------------

class Product_Clothes_Tops_US(models.Model):
    item_brand = models.CharField(max_length=35, null = True)
    item_title = models.CharField(max_length=35, null = True)
    item_material_composition = models.CharField(max_length=80, blank=True, null = True, default="No information")
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unisex', 'Unisex'),
    ('Kids', 'Kids'),
    )
    item_gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null = True)
    CATEGORY_CHOICES = (
    ('Sweatshirt', 'Sweatshirt'),
    ('Hoodies', 'Hoodies'),
    ('Jumper', 'Jumper'),
    ('Jacket', 'Jacket'),
    ('Cardigan', 'Cardigan'),
    ('Short', 'Short'),
    )

    item_category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, null = True)
    item_asin = models.CharField(max_length=40, null = True)
    item_size = models.CharField(max_length=4, null = True)
    item_price = models.DecimalField(help_text='Price of product even with decimals', max_digits=10, decimal_places=2, null = True)
    CURRENCY_CHOICES = (
    ('EUR', 'EUR'),
    ('GPB', 'GPB'),
    ('USD', 'USD'),
    )
    item_color = models.CharField(max_length=60, null = True)
    item_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null = True, default="USD")
    item_width = models.FloatField(default=52, help_text='Use width in inches', null = True)
    item_height = models.FloatField(default=72, help_text='Use height in inches', null = True)
    item_url = models.URLField(help_text='To add size to link on Amazon - use Short links', max_length=500, null = True)
    item_seller = models.CharField(max_length=25, null = True, default="Amazon")
    image_main = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True)
    image_secondary = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True, blank = True)
    image_third = models.ImageField(help_text='600 x 900', max_length=200, upload_to='images/', null = True, blank = True)
    CONTINENT_CHOICES = (
    ('Unites States', 'United States'),
    ('Canada', 'Canada'),
    )
    item_continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES, null = True, default="United States")
    upload_date = models.DateTimeField(default=datetime.now, null = True)

    def __str__(self):
        return self.item_title

class ProductClothesTopsUSProxy(Product_Clothes_Tops_US):
    class Meta:
        proxy = True
