# Generated by Django 5.0.4 on 2024-06-01 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macroNutrientApp', '0015_mealentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
    ]
