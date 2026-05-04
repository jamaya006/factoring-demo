from django import forms
from .models import Project, PhysicalTake, DailyClose, ZoneClose, ImportBatch

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','client','description','start_date','end_date','status']

class ImportBatchForm(forms.ModelForm):
    class Meta:
        model = ImportBatch
        fields = ['project','source_file']

class PhysicalTakeForm(forms.ModelForm):
    class Meta:
        model = PhysicalTake
        exclude = ['captured_by','created_at']

class DailyCloseForm(forms.ModelForm):
    class Meta:
        model = DailyClose
        fields = ['project','date','reviewed_assets','incidents','comments']

class ZoneCloseForm(forms.ModelForm):
    class Meta:
        model = ZoneClose
        fields = ['project','location','expected_assets','reviewed_assets','incidents','comments']
