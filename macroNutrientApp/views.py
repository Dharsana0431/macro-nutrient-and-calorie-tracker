from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"home.html")

def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST.get("role")
        
        usersave=Register(name=name,email=email,password=password)
        usersave.save()
        if role=="user":
            return redirect('login')
        else :
            return redirect("adminlogin")
    return render(request,"reg.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.get(email=email,password=password)
        return redirect('userlogin')
    return render(request,"login.html")

def adminlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.get(email=email,password=password)
        return redirect("admins")    
    return render(request,"adminlogin.html")

@login_required
def mealentry(request):
    if request.method == 'POST':
        food_name = request.POST.get('food')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        
        try:
            food = Food.objects.get(name=food_name)
        except Food.DoesNotExist:
            messages.error(request, 'Food item not found.')
            return redirect('mealentry')
        
        meal_entry = MealEntry(user=request.user, food=food, quantity=quantity, date=date)
        meal_entry.save()

     
        return HttpResponse("Meal entry submitted successfully!")
    else:
        return render(request, 'mealentry.html')

    
@login_required
def nutritionalanalysis(request):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    try:
        meal_entries = MealEntry.objects.filter(user=request.user)

        for entry in meal_entries:
            total_calories += entry.food.calories * entry.quantity
            total_protein += entry.food.protein * entry.quantity
            total_carbs += entry.food.carbs * entry.quantity
            total_fat += entry.food.fat * entry.quantity
    except MealEntry.DoesNotExist:
        meal_entries = []

    context = {
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_carbs': total_carbs,
        'total_fat': total_fat,
    }
    return render(request, 'nutritionalanalysis.html', context)


@login_required
def summary(request):
    total_meals = 0
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    meal_entries = MealEntry.objects.filter(user=request.user)

    total_meals = meal_entries.count()
    for entry in meal_entries:
        total_calories += entry.food.calories * entry.quantity
        total_protein += entry.food.protein * entry.quantity
        total_carbs += entry.food.carbs * entry.quantity
        total_fat += entry.food.fat * entry.quantity

    context = {
        'total_meals': total_meals,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_carbs': total_carbs,
        'total_fat': total_fat,
    }

    return render(request, 'summary.html', context)

def userlogin(request):
    return render(request,"userlogin.html")


@login_required
def mealplanning(request):
    meal_plans = MealPlanning.objects.filter(user=request.user)
    if request.method == 'POST':
        meal = request.POST.get('meal')
        food = request.POST.get('food')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')

        meal_plan = MealPlanning(user=request.user, meal=meal, food=food, quantity=quantity, date=date)
        meal_plan.save()
        return HttpResponse('Meal planned successfully')
    return redirect('mealplanning')


@login_required
def goals(request):
    if request.method == 'POST':
        goal_type = request.POST.get('goaltype')
        target_metrics = request.POST.get('targetmetrics')
        timeframe = request.POST.get('timeframe')

        goal_setting=GoalSetting(user=request.user,goal_type=goal_type, target_metrics=target_metrics, timeframe=timeframe)
        goal_setting.save()
        return HttpResponse("Goal set successfully")
    else:
        return render(request,'goals.html')
       
        

def fooddatabase(request):
    foods = Food.objects.all()
    return render(request, 'fooddatabase.html', {'foods': foods})


def admins(request):
    details=Register.objects.all()
    mealentries=MealEntry.objects.all()
    fooddetails=Food.objects.all()
    return render(request,"admins.html",{'details':details,'mealentries':mealentries,'fooddetails':fooddetails})


def update(request,id):
    u=Food.objects.filter(id=id)
    if request.method=="POST":
        name=request.POST['name']
        calories=request.POST['calories']
        proteins=request.POST['proteins']
        carbs=request.POST['carbs']
        fat=request.POST['fat']
        Food.objects.filter(id=id).update(name=name,calories=calories,protein=proteins,carbs=carbs,fat=fat)
        return redirect('admins')
    return render(request,"update.html",{'u':u})

def delete(request,id):
    emp=Food.objects.get(id=id)
    emp.delete()
    return redirect('admins')

def addfood(request):
    if request.method=="POST":
        name=request.POST['name']
        calories=request.POST['calories']
        proteins=request.POST['proteins']
        carbs=request.POST['carbs']
        fat=request.POST['fat']
        foodsave=Food(name=name,calories=calories,protein=proteins,carbs=carbs,fat=fat)
        foodsave.save()
        return redirect('admins')
    return render(request,"addfood.html")