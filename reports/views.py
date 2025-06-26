from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MalariaCaseReportForm
from .models import MalariaCaseReport

@login_required
def report_create(request):
    if request.method == 'POST':
        form = MalariaCaseReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            return redirect('dashboard:home')
    else:
        form = MalariaCaseReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def report_list(request):
    reports = MalariaCaseReport.objects.filter(reporter=request.user)
    return render(request, 'reports/report_list.html', {'reports': reports})
