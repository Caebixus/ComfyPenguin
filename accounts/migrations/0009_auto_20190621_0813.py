# Generated by Django 2.1.5 on 2019-06-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190621_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclothes',
            name='image_main',
            field=models.ImageField(blank=True, default='imagesUser/boy.png', help_text='600 x 900', max_length=200, null=True, upload_to='imagesUser/'),
        ),
    ]