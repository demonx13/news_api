from django.shortcuts import render
from rest_framework.views import APIView, Response
# Create your views here.
from .permissions import PublicPermissions
from src.news.models import News, Category
from .services import data_from_page, page_validator
from .serializers import CategoriesSerializer, NewsListSerializer

my_content_type = "application/json; charset=utf-8"


class NewsByCategory(APIView):
    """
    """
    permission_classes = [PublicPermissions]

    def get(self, request, pk):

        try:
            queryset = News.objects.filter(category_id=pk)
            page = page_validator(self.request.query_params.get('page', 1))

            # if param_page == "" :
            #     page = 1
            # else:
            #     page = int(self.request.query_params.get('page', 1))
            # if isinstance(page) == None or isinstance(page, str):

            queryset = data_from_page(queryset, page)
            serializer = NewsListSerializer(queryset, many=True)
            data = {'code': 0, 'list': serializer.data}
            status = 200
        except Exception as err:
            data = {'code': 1, 'message': str(err)}
            status = 400
        return Response(data=data, status=status)


class CategoryListNews(APIView):

    permission_classes = [PublicPermissions]

    def get(self, request):
        try:
            queryset = Category.objects.all()
            serializer = CategoriesSerializer(queryset, many=True)
            data = {'code': 0, 'list': serializer.data}
            status = 200
        except Exception as err:
            data = {'code': 1, 'message': str(err)}
            status = 400
        return Response(data=data, status=status)
