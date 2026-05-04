from rest_framework import generics, permissions
from inventory.models import AssetMaster, PhysicalTake, Finding
from .serializers import AssetSerializer, PhysicalTakeSerializer, FindingSerializer

class AssetList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer
    def get_queryset(self):
        return AssetMaster.objects.filter(project_id=self.kwargs['project_id'])

class TakeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PhysicalTakeSerializer

class FindingList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FindingSerializer
    def get_queryset(self):
        return Finding.objects.filter(project_id=self.kwargs['project_id'])
