from django.urls import path
from .views import AssetList, TakeCreate, FindingList
urlpatterns = [
    path('projects/<int:project_id>/assets/', AssetList.as_view()),
    path('takes/', TakeCreate.as_view()),
    path('projects/<int:project_id>/findings/', FindingList.as_view()),
]
