from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from .forms import ReportForm

# Create your views here.

def home(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'waste/home.html', {'reports': reports})

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'waste/create.html', {'form': form})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'waste/detail.html', {'report': report})