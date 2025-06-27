from django.contrib import admin
from .models import Neighborhood, RiskZone, HealthFacility, WaterBody

@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk_level', 'population', 'last_updated')
    list_filter = ('risk_level', 'last_updated')
    search_fields = ('name',)
    readonly_fields = ('last_updated',)

@admin.register(RiskZone)
class RiskZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk_level', 'created_at', 'updated_at')
    list_filter = ('risk_level', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(HealthFacility)
class HealthFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'facility_type', 'contact_number', 'is_active')
    list_filter = ('facility_type', 'is_active')
    search_fields = ('name', 'address', 'contact_number', 'email')
    readonly_fields = ()

@admin.register(WaterBody)
class WaterBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'water_type', 'is_stagnant')
    list_filter = ('water_type', 'is_stagnant')
    search_fields = ('name',)
    readonly_fields = ()
