from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class MyClothes(models.Model):
    item_title = models.CharField(max_length=255)

    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    )
    item_gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null = True)

    CATEGORY_CHOICES_COUNTRY = (
    ('United States', 'United States'),
    )
    item_country = models.CharField(max_length=255, choices=CATEGORY_CHOICES_COUNTRY, null = True)

    CATEGORY_CHOICES = (
    ('Sweatshirt', 'Sweatshirt'),
    ('Hoodies', 'Hoodies'),
    ('Jumper', 'Jumper'),
    )
    item_category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, null = True)

    item_width = models.FloatField(help_text='Use width in inches', null = True)

    item_length = models.FloatField(help_text='Use length in inches', null = True)

    image_main = models.ImageField(help_text='600 x 900', max_length=200, default="imagesUser/boy.png", upload_to='imagesUser/', null=True, blank=True)

    item_user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_checked = models.BooleanField(default=False)

    upload_date = models.DateTimeField(default=datetime.now, null = True)
    def __str__(self):
        return self.item_title
