# Generated by Django 2.1.5 on 2019-06-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclothes',
            name='item_height',
        ),
        migrations.AddField(
            model_name='myclothes',
            name='item_length',
            field=models.FloatField(help_text='Use length in inches', null=True),
        ),
    ]
