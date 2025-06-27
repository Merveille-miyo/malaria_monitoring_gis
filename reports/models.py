from django.db import models
from django.conf import settings

class MalariaCaseReport(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    latitude = models.FloatField(default=6.6111)
    longitude = models.FloatField(default=20.9394)
    symptoms = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='medium')
    date_reported = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='validated_reports')
    validation_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Report by {self.reporter} on {self.date_reported.strftime('%Y-%m-%d')}"

class Alert(models.Model):
    LEVEL_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        try:
            level_display = self.get_level_display()
        except Exception:
            level_display = self.level
        return f"{self.title} - {level_display}"

class Intervention(models.Model):
    TYPE_CHOICES = (
        ('spraying', 'Mosquito Spraying'),
        ('nets', 'Bed Net Distribution'),
        ('medication', 'Medication Distribution'),
        ('education', 'Public Education'),
        ('testing', 'Testing Campaign'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    intervention_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    latitude = models.FloatField(default=6.6111)
    longitude = models.FloatField(default=20.9394)
    planned_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    resources_needed = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        try:
            status_display = self.get_status_display()
        except Exception:
            status_display = self.status
        return f"{self.title} - {status_display}"
