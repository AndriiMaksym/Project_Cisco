from django.db.models import Avg, ExpressionWrapper, DurationField

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealForm, ActivityForm, WeightEntryForm, CustomUserCreationForm
from .models import Meal, Activity, WeightEntry


# Create your views here.


@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('home_page')
    else:
        form = MealForm()
    return render(request, 'add_meal.html', {'form': form})


@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('home_page')
    else:
        form = ActivityForm()
    return render(request, 'add_activity.html', {'form': form})


@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            return redirect('home_page')
    else:
        form = WeightEntryForm()
    return render(request, 'add_weight.html', {'form': form})


def home_page(request):
    return render(request, 'home_page.html')





def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def data_overview(request):
    if request.user.is_authenticated:
        # Calculate average calories and proteins from meals
        avg_calories = Meal.objects.filter(user=request.user).aggregate(Avg('calories'))['calories__avg'] or 0
        avg_proteins = Meal.objects.filter(user=request.user).aggregate(Avg('proteins'))['proteins__avg'] or 0
        avg_fats = Meal.objects.filter(user=request.user).aggregate(Avg('fats'))['fats__avg'] or 0

        # Calculate average duration and calories burned from activities
        avg_activity_duration = Activity.objects.filter(user=request.user).aggregate(
            avg_duration=ExpressionWrapper(Avg('duration'), output_field=DurationField())
        )['avg_duration'] or 0
        avg_calories_burned = Activity.objects.filter(user=request.user).aggregate(Avg('calories_burned'))['calories_burned__avg'] or 0

        # Calculate average weight
        avg_weight = WeightEntry.objects.filter(user=request.user).aggregate(Avg('weight'))['weight__avg'] or 0

        # Fetch weight entries
        weight_entries = WeightEntry.objects.filter(user=request.user)

        context = {
            'avg_calories': avg_calories,
            'avg_proteins': avg_proteins,
            'avg_fats': avg_fats,
            'avg_activity_duration': avg_activity_duration,
            'avg_calories_burned': avg_calories_burned,
            'avg_weight': avg_weight,
            'weight_entries': weight_entries,
        }
        return render(request, 'data_overview.html', context)
    else:
        return redirect('login')
