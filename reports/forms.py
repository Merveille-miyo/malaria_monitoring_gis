from django import forms
from .models import MalariaCaseReport
from leaflet.forms.widgets import LeafletWidget

class MalariaCaseReportForm(forms.ModelForm):
    class Meta:
        model = MalariaCaseReport
        fields = ('location', 'symptoms', 'severity')
        widgets = {
            'location': LeafletWidget(),
        }
