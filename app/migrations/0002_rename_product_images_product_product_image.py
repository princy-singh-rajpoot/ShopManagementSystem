# Generated by Django 5.0.1 on 2024-02-21 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_images',
            new_name='product_image',
        ),
    ]
