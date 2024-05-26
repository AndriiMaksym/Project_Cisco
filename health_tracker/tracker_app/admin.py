from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Meal, Activity, WeightEntry

admin.site.register(Meal)
admin.site.register(Activity)
admin.site.register(WeightEntry)
