# Generated by Django 2.1.5 on 2019-02-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_product_clothes_item_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_clothes',
            name='item_brand',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='product_clothes',
            name='image_main',
            field=models.ImageField(help_text='600 x 900', max_length=200, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product_clothes',
            name='image_secondary',
            field=models.ImageField(blank=True, help_text='600 x 900', max_length=200, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product_clothes',
            name='image_third',
            field=models.ImageField(blank=True, help_text='600 x 900', max_length=200, null=True, upload_to='images/'),
        ),
    ]