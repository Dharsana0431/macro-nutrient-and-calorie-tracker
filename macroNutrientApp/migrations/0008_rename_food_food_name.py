# Generated by Django 5.0.4 on 2024-05-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macroNutrientApp', '0007_rename_name_food_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food',
            new_name='name',
        ),
    ]
