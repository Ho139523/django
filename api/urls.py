from django.urls import path, include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register('', views.ArticleAPIView)

app_name='api'

urlpatterns = [
    path('v1/', include(router.urls)),
]
