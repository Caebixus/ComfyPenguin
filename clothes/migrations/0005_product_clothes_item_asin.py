# Generated by Django 2.1.3 on 2018-12-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20181209_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_clothes',
            name='item_asin',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]