from django.contrib.gis.db import models
from django.conf import settings

class MalariaCaseReport(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.PointField()
    symptoms = models.TextField()
    severity = models.CharField(max_length=50)
    date_reported = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f"Report by {self.reporter} on {self.date_reported.strftime('%Y-%m-%d')}"
