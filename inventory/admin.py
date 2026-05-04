from django.contrib import admin
from .models import *

for model in [Project, Location, ImportBatch, AssetMaster, Assignment, PhysicalTake, TakePhoto, DailyClose, Finding, ZoneClose, AuditLog]:
    admin.site.register(model)
