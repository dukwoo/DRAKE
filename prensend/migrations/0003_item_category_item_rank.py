# Generated by Django 4.2 on 2023-05-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prensend', '0002_remove_item_brand_item_image_item_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='rank',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]