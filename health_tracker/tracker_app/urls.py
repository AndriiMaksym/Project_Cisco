from django.urls import path, include
from . import views, admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_meal/', views.add_meal, name="add_meal"),
    path("add_activity/", views.add_activity, name="add_activity"),
    path("add_weight/", views.add_weight, name="add_weight"),
    path('data_overview/', views.data_overview, name='data_overview'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
