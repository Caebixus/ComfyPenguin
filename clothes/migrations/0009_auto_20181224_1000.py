# Generated by Django 2.1.3 on 2018-12-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_auto_20181216_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_clothes',
            name='image_main',
            field=models.ImageField(max_length=200, null=True, upload_to='images/'),
        ),
    ]