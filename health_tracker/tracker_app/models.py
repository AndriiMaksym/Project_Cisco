from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=50, null=True)
    calories = models.IntegerField(null=True)
    proteins = models.FloatField(null=True)
    fats = models.FloatField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"

    # Main Extra options configuration for model

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"
        ordering = ['-date', 'user']  # Сортировка по дате (убывание)


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity_type = models.CharField(max_length=50)
    duration = models.DurationField(null=True)
    calories_burned = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ['-date', 'user']  # Сортировка по дате (убывание)


class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.weight}kg on {self.date}"

    class Meta:
        verbose_name = "WeigtEntry"
        ordering = ['-date', 'user']  # Сортировка по дате (убывание)
