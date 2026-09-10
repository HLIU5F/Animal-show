from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Animal, Category
admin.site.register(Animal)
admin.site.register(Category)