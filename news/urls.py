from django.urls import path
from .views import home, description, category
from django.conf import settings
from django.conf.urls.static import static

app_name='news'
urlpatterns = [
    path('', home, name='home'),
    path('page/<int:page>', home, name='home'),
    path('article/<slug:slug>/', description, name='description'),
    path('category/<slug:slug>/', category, name='category'),
    path('category/<slug:slug>/page/<int:page>', category, name='category')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
