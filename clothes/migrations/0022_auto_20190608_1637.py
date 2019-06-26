# Generated by Django 2.1.5 on 2019-06-08 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0021_auto_20190606_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Clothes_Tops_US',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_brand', models.CharField(max_length=35, null=True)),
                ('item_title', models.CharField(max_length=35, null=True)),
                ('item_material_composition', models.CharField(blank=True, default='No information', max_length=80, null=True)),
                ('item_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex'), ('Kids', 'Kids')], max_length=40, null=True)),
                ('item_category', models.CharField(choices=[('Sweatshirt', 'Sweatshirt'), ('Hoodies', 'Hoodies'), ('Jumper', 'Jumper'), ('Jacket', 'Jacket'), ('Cardigan', 'Cardigan'), ('Short', 'Short')], max_length=40, null=True)),
                ('item_asin', models.CharField(max_length=40, null=True)),
                ('item_size', models.CharField(max_length=4, null=True)),
                ('item_price', models.DecimalField(decimal_places=2, help_text='Price of product even with decimals', max_digits=10, null=True)),
                ('item_color', models.CharField(max_length=60, null=True)),
                ('item_currency', models.CharField(choices=[('EUR', 'EUR'), ('GPB', 'GPB'), ('USD', 'USD')], default='USD', max_length=3, null=True)),
                ('item_width', models.FloatField(default=52, help_text='Use width in inches', null=True)),
                ('item_height', models.FloatField(default=72, help_text='Use height in inches', null=True)),
                ('item_url', models.URLField(help_text='To add size to link on Amazon - use Short links', max_length=150, null=True)),
                ('item_seller', models.CharField(default='Amazon', max_length=25, null=True)),
                ('image_main', models.ImageField(help_text='600 x 900', max_length=200, null=True, upload_to='images/')),
                ('image_secondary', models.ImageField(blank=True, help_text='600 x 900', max_length=200, null=True, upload_to='images/')),
                ('image_third', models.ImageField(blank=True, help_text='600 x 900', max_length=200, null=True, upload_to='images/')),
                ('item_continent', models.CharField(choices=[('Unites States', 'United States'), ('Canada', 'Canada')], default='United States', max_length=20, null=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product_clothes_tops',
            name='item_height',
            field=models.FloatField(default=72, help_text='Use height in centimeters', null=True),
        ),
        migrations.AlterField(
            model_name='product_clothes_tops',
            name='item_width',
            field=models.FloatField(default=52, help_text='Use width in centimeters', null=True),
        ),
    ]
