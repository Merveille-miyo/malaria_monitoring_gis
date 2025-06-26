from django.contrib import admin
from .models import MalariaCaseReport

@admin.register(MalariaCaseReport)
class MalariaCaseReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'date_reported', 'severity', 'validated')
    list_filter = ('validated', 'severity')
    search_fields = ('reporter__username', 'symptoms')
