from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category, News
from .serializers import CategorySerializer, ListCategorySerializer
from .permissions import PublicPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .services import data_from_page
from django.shortcuts import redirect


def ListNewsRedirect(request, pk):
    return redirect(f'http://127.0.0.1:8000/v1/news/categories/{pk}/news/1')


class ListCategories(APIView):
    """
    """
    permission_classes = [PublicPermissions]

    def get(self, request):
        """
        Return a list of all users.
        """
        data = {}
        categories = [{category.id: category.themes} for category in Category.objects.all()]
        if categories:
            data.update({'code': 0, 'list': categories})
        return Response(data, status=200)


class NewsByCategory(APIView):
    """
    """
    permission_classes = [PublicPermissions]

    def get(self, request, pk, page=1):
        data = {}
        news = [{news.id: news.title} for news in News.objects.filter(category_id=pk)]
        news = data_from_page(news, page=page)
        if news:
            data.update({'code': 0, 'list': news})

        return Response(data, status=200)


class CategoryViewSet(viewsets.ViewSet):
    """
    """

    permission_classes = [PublicPermissions]

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ListCategoryViewSet(viewsets.ViewSet):

    permission_classes = [PublicPermissions]

    def get(self, request):
        queryset = Category.objects.all()
        serializer = ListCategorySerializer(queryset, many=True)
        return Response(serializer.data)
