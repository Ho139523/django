from news.models import Articles
from django.conf import settings
from .serializer import ArticleSerializer
from rest_framework import viewsets


class ArticleAPIView(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

