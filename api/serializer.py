from rest_framework import serializers
from news.models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ["title", "writer", "description", "image", "published", "status"]