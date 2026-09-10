from django.urls import path
from . import views

app_name = 'animals'
urlpatterns = [
    path('', views.animal_list, name='list'),
    path('add/', views.animal_add, name='add'),
    path('detail/<int:pk>/', views.animal_detail, name='animal_detail'),

]