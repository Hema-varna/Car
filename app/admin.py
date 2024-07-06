from django.contrib import admin
from app.models import CarTable

# Register your models here.
@admin.register(CarTable)
class carregister(admin.ModelAdmin):
    list_display=['cname','cimage']

