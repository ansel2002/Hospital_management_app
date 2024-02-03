# Generated by Django 4.1.2 on 2024-01-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0002_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('appointment_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]