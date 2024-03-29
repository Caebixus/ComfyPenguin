# Generated by Django 2.1.3 on 2018-12-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20181209_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_clothes',
            name='item_category',
            field=models.CharField(blank=True, choices=[('Sweatshirt', 'Sweatshirt'), ('Hoodies', 'Hoodies'), ('Jumper', 'Jumper')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product_clothes',
            name='item_gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex')], max_length=40, null=True),
        ),
    ]
