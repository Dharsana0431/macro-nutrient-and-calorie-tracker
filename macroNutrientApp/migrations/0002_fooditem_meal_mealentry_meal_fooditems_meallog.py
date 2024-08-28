# Generated by Django 5.0.4 on 2024-05-27 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macroNutrientApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fats', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MealEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='macroNutrientApp.fooditem')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='macroNutrientApp.meal')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='fooditems',
            field=models.ManyToManyField(through='macroNutrientApp.MealEntry', to='macroNutrientApp.fooditem'),
        ),
        migrations.CreateModel(
            name='MealLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='macroNutrientApp.meal')),
            ],
        ),
    ]