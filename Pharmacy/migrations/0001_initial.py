# Generated by Django 4.2.7 on 2024-01-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('order_notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=50)),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('expiry_date', models.DateField()),
                ('provider_status', models.BooleanField()),
                ('latex_free_status', models.BooleanField()),
                ('medication_route', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.store')),
            ],
        ),
    ]