from django import forms
from django.contrib.auth.models import User
from .models import Meal, Activity, WeightEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['date', 'meal_type', 'calories', 'proteins', 'fats']

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'activity_type', 'duration', 'calories_burned']

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['date', 'weight']

    def __init__(self, *args, **kwargs):
        super(WeightEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
