from django.contrib import admin
from .models import ScheduleModel, ClientModel

@admin.register(ScheduleModel)
class SheludeModelAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'age', 'start_time', 'end_time')
    search_fields = ('weekday', 'age', 'start_time', 'end_time')
    list_filter = ('weekday', 'age', 'start_time', 'end_time')

@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('name', 'phone')