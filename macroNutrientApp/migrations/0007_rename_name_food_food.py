# Generated by Django 5.0.4 on 2024-05-29 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macroNutrientApp', '0006_mealplanning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='name',
            new_name='food',
        ),
    ]
