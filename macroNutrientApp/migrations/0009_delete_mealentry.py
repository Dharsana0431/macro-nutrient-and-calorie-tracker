# Generated by Django 5.0.4 on 2024-05-29 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macroNutrientApp', '0008_rename_food_food_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MealEntry',
        ),
    ]
