from django import forms
from .models import MalariaCaseReport, Alert, Intervention

class MalariaCaseReportForm(forms.ModelForm):
    class Meta:
        model = MalariaCaseReport
        fields = ('latitude', 'longitude', 'symptoms', 'severity')
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Latitude (e.g., 6.6111)'}),
            'longitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Longitude (e.g., 20.9394)'}),
            'symptoms': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the symptoms observed...'}),
        }

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('title', 'message', 'level', 'latitude', 'longitude')
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Latitude'}),
            'longitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Longitude'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ('title', 'description', 'intervention_type', 'latitude', 'longitude', 'planned_date', 'resources_needed', 'budget')
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Latitude'}),
            'longitude': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Longitude'}),
            'planned_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'resources_needed': forms.Textarea(attrs={'rows': 3}),
        }
