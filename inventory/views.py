from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from PIL import Image
import openpyxl
from .forms import DailyCloseForm, ImportBatchForm, PhysicalTakeForm, ProjectForm
from .models import AssetMaster, PhysicalTake, Project, TakePhoto
from .services.importer import import_assets_from_excel
from .services.reconciliation import run_reconciliation

@login_required
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'inventory/dashboard.html', {'projects': projects})

@login_required
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        p = form.save(commit=False); p.created_by = request.user; p.save(); return redirect('dashboard')
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Nuevo proyecto'})

@login_required
def import_master(request):
    form = ImportBatchForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        b = form.save(); import_assets_from_excel(b); return redirect('dashboard')
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Importar maestro'})

@login_required
def take_capture(request):
    form = PhysicalTakeForm(request.POST or None)
    if form.is_valid():
        take = form.save(commit=False); take.captured_by = request.user; take.save()
        for f in request.FILES.getlist('photos'):
            img = Image.open(f).convert('RGB'); img.thumbnail((1600, 1600))
            buff = BytesIO(); img.save(buff, format='JPEG', quality=75)
            compressed = InMemoryUploadedFile(buff, 'ImageField', f'{timezone.now().timestamp()}.jpg', 'image/jpeg', buff.tell(), None)
            TakePhoto.objects.create(take=take, image=compressed)
        return redirect('take_capture')
    return render(request, 'inventory/take_capture.html', {'form': form})

@login_required
def run_reconciliation_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    run_reconciliation(project)
    return redirect('dashboard')

@login_required
def export_report(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = 'resumen'; ws.append(['Proyecto', project.name])
    ws.append(['Total activos', AssetMaster.objects.filter(project=project).count()])
    ws.append(['Total tomas', PhysicalTake.objects.filter(project=project).count()])
    ws2 = wb.create_sheet('toma_fisica'); ws2.append(['codigo','estado','usuario'])
    for t in PhysicalTake.objects.filter(project=project): ws2.append([t.observed_asset_code, t.verification_status, t.captured_by.username])
    output = BytesIO(); wb.save(output); output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=reporte_{project.id}.xlsx'
    return response
