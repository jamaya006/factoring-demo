from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from inventory.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', dashboard, name='dashboard'),
    path('inventory/', include('inventory.urls')),
    path('api/', include('inventory.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
