import uuid
from django.conf import settings
from django.db import models

class Project(models.Model):
    STATUS = [('draft','Borrador'),('active','Activo'),('closed','Cerrado')]
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

class Location(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

class ImportBatch(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    source_file = models.FileField(upload_to='imports/')
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)
    errors = models.TextField(blank=True)

class AssetMaster(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    source_sheet = models.CharField(max_length=100)
    source_row = models.IntegerField()
    source_file_name = models.CharField(max_length=255)
    cuenta = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=255, blank=True)
    fecha_adquisicion = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=100, blank=True)
    vida_util = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    observacion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    grupo_contable = models.CharField(max_length=255, blank=True)
    costo_responsable = models.CharField(max_length=255, blank=True)
    cuenta_depreciacion = models.CharField(max_length=255, blank=True)
    historico_revaluo = models.CharField(max_length=255, blank=True)
    modelo = models.CharField(max_length=255, blank=True)
    anio_fabricacion = models.CharField(max_length=50, blank=True)
    numero_serie = models.CharField(max_length=255, blank=True)
    proveedor = models.CharField(max_length=255, blank=True)
    num_activo = models.CharField(max_length=150, blank=True)
    tipo_orden_pago = models.CharField(max_length=255, blank=True)
    numero_orden_pago_sum = models.CharField(max_length=255, blank=True)
    asset_code = models.CharField(max_length=255)
    internal_key = models.UUIDField(default=uuid.uuid4, editable=False)
    plate_code = models.CharField(max_length=255, blank=True)
    custodian_name = models.CharField(max_length=255, blank=True)
    status_expected = models.CharField(max_length=50, default='active')
    class Meta:
        unique_together = ('project','asset_code')

class Assignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=120, blank=True)
    custodian = models.CharField(max_length=255, blank=True)
    range_start = models.CharField(max_length=120, blank=True)
    range_end = models.CharField(max_length=120, blank=True)

class PhysicalTake(models.Model):
    STATUS = [('found','Encontrado'),('not_found','No encontrado'),('no_tag','Sin placa'),('damaged','Dañado'),('obsolete','Obsoleto'),('surplus','Sobrante'),('inconsistent','Inconsistente')]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetMaster, null=True, blank=True, on_delete=models.SET_NULL)
    captured_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    observed_asset_code = models.CharField(max_length=255, blank=True)
    observed_plate_code = models.CharField(max_length=255, blank=True)
    qr_value = models.CharField(max_length=255, blank=True)
    barcode_value = models.CharField(max_length=255, blank=True)
    observed_description = models.TextField(blank=True)
    observed_location = models.CharField(max_length=255, blank=True)
    observed_custodian = models.CharField(max_length=255, blank=True)
    verification_status = models.CharField(max_length=20, choices=STATUS)
    condition = models.CharField(max_length=120, blank=True)
    observations = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TakePhoto(models.Model):
    take = models.ForeignKey(PhysicalTake, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='takes/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

class DailyClose(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    reviewed_assets = models.IntegerField(default=0)
    incidents = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    class Meta: unique_together = ('user','project','date')

class Finding(models.Model):
    TYPES = [('match','Match'),('missing','Missing'),('surplus','Surplus'),('location_diff','Location Diff'),('custodian_diff','Custodian Diff'),('tag_diff','Tag Diff'),('damaged','Damaged'),('obsolete','Obsolete'),('duplicate_take','Duplicate Take'),('other','Other')]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    take = models.ForeignKey(PhysicalTake, null=True, blank=True, on_delete=models.SET_NULL)
    asset = models.ForeignKey(AssetMaster, null=True, blank=True, on_delete=models.SET_NULL)
    finding_type = models.CharField(max_length=30, choices=TYPES)
    notes = models.TextField(blank=True)
    reviewed_status = models.CharField(max_length=20, default='pending')
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    reviewed_at = models.DateTimeField(null=True, blank=True)

class ZoneClose(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    closed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    expected_assets = models.IntegerField(default=0)
    reviewed_assets = models.IntegerField(default=0)
    incidents = models.TextField(blank=True)
    comments = models.TextField(blank=True)

class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
    event = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
