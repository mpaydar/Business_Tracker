from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Holiday/', views.Holiday, name="home"),
    path('DataBase/', views.DataBase, name="database"),


]