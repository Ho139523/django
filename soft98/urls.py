from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('api/', include('api.urls'), name='api'),
    path('bankgateways/', az_bank_gateways_urls()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
