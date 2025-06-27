import json
from django.shortcuts import render
from django.core.serializers import serialize
from .models import RiskZone, Neighborhood, HealthFacility

def map_view(request):
    """Interactive map view showing risk zones and health facilities"""
    # Get risk zones
    risk_zones = RiskZone.objects.all()
    risk_zones_geojson = json.loads(serialize('geojson', risk_zones))
    
    # Get neighborhoods
    neighborhoods = Neighborhood.objects.all()
    neighborhoods_geojson = json.loads(serialize('geojson', neighborhoods))
    
    # Get health facilities
    health_facilities = HealthFacility.objects.filter(is_active=True)
    health_facilities_geojson = json.loads(serialize('geojson', health_facilities))
    
    context = {
        'risk_zones_geojson': json.dumps(risk_zones_geojson),
        'neighborhoods_geojson': json.dumps(neighborhoods_geojson),
        'health_facilities_geojson': json.dumps(health_facilities_geojson),
    }
    
    return render(request, 'gisdata/map.html', context)

