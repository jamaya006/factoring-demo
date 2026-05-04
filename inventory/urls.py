from django.urls import path
from . import views

urlpatterns = [
    path('projects/new/', views.project_create, name='project_create'),
    path('imports/new/', views.import_master, name='import_master'),
    path('takes/capture/', views.take_capture, name='take_capture'),
    path('projects/<int:project_id>/reconcile/', views.run_reconciliation_view, name='run_reconciliation'),
    path('projects/<int:project_id>/export/', views.export_report, name='export_report'),
]
