import json
from django.shortcuts import render
from django.core.serializers import serialize
from .models import RiskZone  # Make sure RiskZone is imported

def malaria_map(request):
    geojson_data = json.loads(serialize('geojson', RiskZone.objects.all()))
    return render(request, 'gisdata/map.html', {'geojson': json.dumps(geojson_data)})

