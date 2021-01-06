from rest_framework import serializers
from .models import News, Category


# class NewsSerializer(serializers.ModelSerializer):
#     """Serializer for news
#     """
#
#     class Meta:
#         model = News
#         fields = ['__all__']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'name')


class ListCategorySerializer(serializers.ModelSerializer):

    code = serializers.SerializerMethodField()
    list = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('code', 'list')

    def get_code(self, obj):
        return 0

    def get_list(self, obj):
        return 1

# class ListNewsSerializer(serializers.ListSerializer):
#     """
#     """
#
#     class Meta:
#
#         model = Category
#         fields = ('__all__')
