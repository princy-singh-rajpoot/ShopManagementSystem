# Generated by Django 5.0.1 on 2024-02-21 08:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('S', 'Sunglasses'), ('C', 'Contactlenses'), ('E', 'Eyeeglasses'), ('G', 'Goggles')], max_length=2)),
                ('product_images', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman and Nicobar Island', 'Andaman and Nicobar Island'), (' Andhra Pradesh ', 'Andhra Pradesh '), ('Arunachal Pradesh ', 'Arunachal Pradesh'), ('Assam ', 'Assam'), (' Bihar ', 'Bihar'), ('Chandigarh ', 'Chandigarh'), ('Chhattisgarh ', 'Chhattisgarh'), (' Arunachal Pradesh', 'Arunachal Pradesh'), (' Karnataka ', 'Karnataka'), ('Kerala ', 'Kerala'), (' akshadweep ', 'akshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Maharashtra ', 'Maharashtra'), ('meghalay ', 'meghalay'), ('Mizoram ', 'Mizoram'), ('Nagaland ', 'Nagaland'), ('udisa ', 'udisa'), ('Punjab ', 'Punjab'), ('Rajasthan ', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Haryana ', 'Haryana'), ('Delhi ', 'Delhi'), ('Goa ', 'Goa'), ('Gujarat', 'Gujarat'), ('Himachal Pradesh ', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Tamilnadu ', 'Tamilnadu'), ('Telangana', 'Telangana'), ('Tripura ', 'Tripura'), ('Uttrakhand ', 'Uttrakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
