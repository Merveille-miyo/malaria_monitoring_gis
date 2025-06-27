from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import MalariaCaseReportForm, AlertForm, InterventionForm
from .models import MalariaCaseReport, Alert, Intervention

@login_required
def report_create(request):
    if request.user.role != 'healthworker':
        messages.error(request, 'Only health workers can submit case reports.')
        return redirect('dashboard:home')
        
    if request.method == 'POST':
        form = MalariaCaseReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            
            # Trigger alert for high severity cases
            if report.severity in ['high', 'critical']:
                Alert.objects.create(
                    title=f"High Severity Malaria Case Reported",
                    message=f"A {report.severity} severity case was reported in the area.",
                    level='high' if report.severity == 'high' else 'critical',
                    location=report.location,
                    created_by=request.user
                )
            
            messages.success(request, 'Case report submitted successfully!')
            return redirect('reports:report_list')
    else:
        form = MalariaCaseReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def report_list(request):
    if request.user.role == 'healthworker':
        reports = MalariaCaseReport.objects.filter(reporter=request.user)
    elif request.user.role in ['medofficer', 'analyst']:
        reports = MalariaCaseReport.objects.all()
    else:
        reports = MalariaCaseReport.objects.none()
    
    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(MalariaCaseReport, pk=pk)
    
    # Check permissions
    if request.user.role == 'healthworker' and report.reporter != request.user:
        messages.error(request, 'You can only view your own reports.')
        return redirect('reports:report_list')
    
    return render(request, 'reports/report_detail.html', {'report': report})

@login_required
def report_validate(request, pk):
    if request.user.role not in ['medofficer', 'analyst']:
        messages.error(request, 'Only medical officers and analysts can validate reports.')
        return redirect('reports:report_list')
    
    report = get_object_or_404(MalariaCaseReport, pk=pk)
    
    if request.method == 'POST':
        report.validated = True
        report.validated_by = request.user
        report.validation_date = timezone.now()
        report.notes = request.POST.get('notes', '')
        report.save()
        
        messages.success(request, 'Report validated successfully!')
        return redirect('reports:report_list')
    
    return render(request, 'reports/report_validate.html', {'report': report})
