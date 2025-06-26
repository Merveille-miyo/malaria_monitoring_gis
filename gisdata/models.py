from django.contrib.gis.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    polygon = models.PolygonField()
    risk_level = models.CharField(max_length=20, choices=(
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ), default='low')

    def __str__(self):
        return f"{self.name} ({self.risk_level})"
