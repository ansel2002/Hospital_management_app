# Generated by Django 4.1.2 on 2024-01-30 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_remove_patient_assigneddoctor_remove_patient_user_and_more'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
