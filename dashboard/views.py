from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from reports.models import MalariaCaseReport, Alert, Intervention
from gisdata.models import Neighborhood, RiskZone, HealthFacility
import json

@login_required
def home(request):
    """Role-based dashboard home view"""
    context = {}
    
    if request.user.role == 'healthworker':
        # Health Worker Dashboard
        recent_reports = MalariaCaseReport.objects.filter(
            reporter=request.user
        ).order_by('-date_reported')[:5]
        context['recent_reports'] = recent_reports
        
    elif request.user.role == 'medofficer':
        # Medical Officer Dashboard
        pending_reports = MalariaCaseReport.objects.filter(validated=False).count()
        high_risk_areas = RiskZone.objects.filter(risk_level__in=['high', 'critical']).count()
        active_alerts = Alert.objects.filter(is_active=True).count()
        
        recent_reports = MalariaCaseReport.objects.filter(validated=False).order_by('-date_reported')[:10]
        
        context.update({
            'pending_reports_count': pending_reports,
            'high_risk_areas_count': high_risk_areas,
            'active_alerts_count': active_alerts,
            'recent_reports': recent_reports,
        })
        
    elif request.user.role == 'analyst':
        # Health Analyst Dashboard
        total_cases = MalariaCaseReport.objects.count()
        cases_this_month = MalariaCaseReport.objects.filter(
            date_reported__month=timezone.now().month
        ).count()
        high_risk_areas_count = RiskZone.objects.filter(risk_level__in=['high', 'critical']).count()
        
        context.update({
            'total_cases': total_cases,
            'cases_this_month': cases_this_month,
            'high_risk_areas_count': high_risk_areas_count,
            'trend_percentage': 5.2,  # Placeholder
        })
        
    elif request.user.role == 'publicuser':
        # Public User Dashboard
        low_risk_areas_count = RiskZone.objects.filter(risk_level='low').count()
        medium_risk_areas_count = RiskZone.objects.filter(risk_level='medium').count()
        high_risk_areas_count = RiskZone.objects.filter(risk_level__in=['high', 'critical']).count()
        recent_alerts = Alert.objects.filter(is_active=True).order_by('-created_at')[:5]
        
        context.update({
            'low_risk_areas_count': low_risk_areas_count,
            'medium_risk_areas_count': medium_risk_areas_count,
            'high_risk_areas_count': high_risk_areas_count,
            'recent_alerts': recent_alerts,
        })
    
    return render(request, 'dashboard/home.html', context)

@login_required
def analytics(request):
    """Analytics dashboard for analysts and medical officers"""
    if request.user.role not in ['analyst', 'medofficer']:
        return redirect('dashboard:home')
    
    # Case statistics
    total_cases = MalariaCaseReport.objects.count()
    cases_by_severity = MalariaCaseReport.objects.values('severity').annotate(count=Count('id'))
    
    # Monthly trends
    months = []
    case_counts = []
    for i in range(6):
        month = timezone.now() - timedelta(days=30*i)
        count = MalariaCaseReport.objects.filter(
            date_reported__month=month.month,
            date_reported__year=month.year
        ).count()
        months.append(month.strftime('%b'))
        case_counts.append(count)
    
    # Risk zone statistics
    risk_zones = RiskZone.objects.values('risk_level').annotate(count=Count('id'))
    
    context = {
        'total_cases': total_cases,
        'cases_by_severity': list(cases_by_severity),
        'months': list(reversed(months)),
        'case_counts': list(reversed(case_counts)),
        'risk_zones': list(risk_zones),
    }
    
    return render(request, 'dashboard/analytics.html', context)

@login_required
def trends(request):
    """Trend analysis view"""
    if request.user.role not in ['analyst', 'medofficer']:
        return redirect('dashboard:home')
    
    # Get trend data
    end_date = timezone.now()
    start_date = end_date - timedelta(days=90)
    
    cases = MalariaCaseReport.objects.filter(
        date_reported__range=[start_date, end_date]
    ).extra(
        select={'day': 'date(date_reported)'}
    ).values('day').annotate(count=Count('id')).order_by('day')
    
    context = {
        'cases': list(cases),
    }
    
    return render(request, 'dashboard/trends.html', context)

@login_required
def heatmap(request):
    """Heatmap view for case density"""
    if request.user.role not in ['analyst', 'medofficer']:
        return redirect('dashboard:home')
    
    # Get case locations for heatmap
    cases = MalariaCaseReport.objects.all()
    case_data = []
    
    for case in cases:
        if case.location:
            case_data.append({
                'lat': case.location.y,
                'lng': case.location.x,
                'weight': 1 if case.severity == 'low' else 2 if case.severity == 'medium' else 3 if case.severity == 'high' else 4
            })
    
    context = {
        'case_data': json.dumps(case_data),
    }
    
    return render(request, 'dashboard/heatmap.html', context)

@login_required
def alerts(request):
    """Public alerts view"""
    alerts = Alert.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'dashboard/alerts.html', {'alerts': alerts})

@login_required
def subscribe(request):
    """Subscription management for public users"""
    if request.user.role != 'publicuser':
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        # Handle subscription logic here
        return redirect('dashboard:home')
    
    return render(request, 'dashboard/subscribe.html')
