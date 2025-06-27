from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=6.6111) #type:ignore
     # Center Cameroon
    longitude = models.FloatField(default=20.9394)#type:ignore


    risk_level = models.CharField(max_length=20, choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ), default='low')
    population = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        try:
            risk = self.get_risk_level_display()
        except Exception:
            risk = self.risk_level
        return f"{self.name} ({risk})"

class RiskZone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=6.6111)#type:ignore
    longitude = models.FloatField(default=20.9394)#type:ignore
    risk_level = models.CharField(max_length=20, choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ), default='low')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        try:
            risk = self.get_risk_level_display()
        except Exception:
            risk = self.risk_level
        return f"{self.name} - {risk}"

class HealthFacility(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=6.6111)#type:ignore
    longitude = models.FloatField(default=20.9394)#type:ignore
    facility_type = models.CharField(max_length=50, choices=(
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('health_center', 'Health Center'),
        ('pharmacy', 'Pharmacy'),
        ('laboratory', 'Laboratory'),
    ))
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        try:
            facility = self.get_facility_type_display()
        except Exception:
            facility = self.facility_type
        return f"{self.name} ({facility})"

class WaterBody(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=6.6111)#type:ignore
    longitude = models.FloatField(default=20.9394)#type:ignore
    water_type = models.CharField(max_length=50, choices=(
        ('river', 'River'),
        ('lake', 'Lake'),
        ('pond', 'Pond'),
        ('stream', 'Stream'),
        ('swamp', 'Swamp'),
        ('other', 'Other'),
    ))
    is_stagnant = models.BooleanField(default=False)
    
    def __str__(self):
        try:
            wtype = self.get_water_type_display()
        except Exception:
            wtype = self.water_type
        return f"{self.name} ({wtype})"
