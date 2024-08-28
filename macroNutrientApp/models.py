from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
 

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name

class MealEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.food.name} - {self.date}"


class NutritionalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calories_goal = models.FloatField()
    protein_goal = models.FloatField()
    carbs_goal = models.FloatField()
    fat_goal = models.FloatField()

    def __str__(self):
        return f"{self.user.username}'s Nutritional Information"

class GoalSetting(models.Model):
    GOAL_TYPES = [
        ('weightloss', 'Weight Loss'),
        ('musclegain', 'Muscle Gain'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    target_metrics = models.CharField(max_length=100)
    timeframe = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.username}'s {self.get_goal_type_display()} Goal"

class MealPlanning(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.meal} - {self.food} - {self.date}"