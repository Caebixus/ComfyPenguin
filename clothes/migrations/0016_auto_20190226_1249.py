# Generated by Django 2.1.5 on 2019-02-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0015_product_clothes_item_material_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_clothes',
            name='item_category',
            field=models.CharField(choices=[('Sweatshirt', 'Sweatshirt'), ('Hoodies', 'Hoodies'), ('Jumper', 'Jumper'), ('T-shirt', 'T-shirt')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product_clothes',
            name='item_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex'), ('Kids', 'Kids')], max_length=40, null=True),
        ),
    ]
