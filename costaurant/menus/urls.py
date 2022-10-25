from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view),
    path('', views.index_view),
    path('food/<int:pk>/', views.detail)
]
