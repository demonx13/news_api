from rest_framework import serializers
from src.news.models import Category, News


class CategoriesSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Category
        fields = ('id', 'name')


class NewsListSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = News
        fields = ('id', 'title', 'date', 'shortDescription')
