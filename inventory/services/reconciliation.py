from inventory.models import AssetMaster, PhysicalTake, Finding

def run_reconciliation(project):
    Finding.objects.filter(project=project).delete()
    assets = {a.asset_code:a for a in AssetMaster.objects.filter(project=project)}
    takes = PhysicalTake.objects.filter(project=project)
    seen = set()
    for t in takes:
        code = t.observed_asset_code or (t.asset.asset_code if t.asset else '')
        if code in seen and code:
            Finding.objects.create(project=project, take=t, finding_type='duplicate_take', notes='Código repetido')
        seen.add(code)
        if code and code in assets:
            Finding.objects.create(project=project, take=t, asset=assets[code], finding_type='match')
        elif t.verification_status == 'surplus':
            Finding.objects.create(project=project, take=t, finding_type='surplus')
    taken_codes = {t.observed_asset_code for t in takes if t.observed_asset_code}
    for a in assets.values():
        if a.asset_code not in taken_codes:
            Finding.objects.create(project=project, asset=a, finding_type='missing')
