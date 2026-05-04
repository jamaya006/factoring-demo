from rest_framework import serializers
from inventory.models import AssetMaster, PhysicalTake, Finding

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaster
        fields = ['id','project','asset_code','descripcion','ubicacion','custodian_name']

class PhysicalTakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalTake
        fields = '__all__'

class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = '__all__'
