# Generated by Django 5.0.1 on 2024-03-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'Sunglasses'), ('C', 'Contactlenses'), ('R', 'Readinglasses'), ('G', 'Goggles')], max_length=2),
        ),
    ]
