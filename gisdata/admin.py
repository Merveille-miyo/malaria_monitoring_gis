from django.contrib import admin
from .models import Neighborhood

@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk_level')
    list_filter = ('risk_level',)
