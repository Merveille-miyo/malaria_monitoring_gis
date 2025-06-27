from django.contrib import admin
from .models import MalariaCaseReport, Alert, Intervention

@admin.register(MalariaCaseReport)
class MalariaCaseReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'severity', 'date_reported', 'validated', 'validated_by')
    list_filter = ('severity', 'validated', 'date_reported')
    search_fields = ('reporter__username', 'reporter__first_name', 'reporter__last_name', 'symptoms')
    readonly_fields = ('date_reported',)
    list_per_page = 20

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'created_by', 'created_at', 'is_active')
    list_filter = ('level', 'is_active', 'created_at')
    search_fields = ('title', 'message', 'created_by__username')
    readonly_fields = ('created_at',)
    list_per_page = 20

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('title', 'intervention_type', 'status', 'planned_date', 'created_by')
    list_filter = ('intervention_type', 'status', 'planned_date')
    search_fields = ('title', 'description', 'created_by__username')
    readonly_fields = ('created_at',)
    list_per_page = 20 