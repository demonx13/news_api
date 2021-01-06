from rest_framework.views import APIView, Response
from .permissions import PublicPermissions
from src.news.models import News, Category
from .services import data_from_page, value_validator, value_validator_news
from .serializers import CategoriesSerializer, NewsListSerializer, NewsSerializer
from .schemas import page_param, id_news_param
from drf_yasg.utils import swagger_auto_schema


class NewsByCategory(APIView):
    """
    """
    permission_classes = [PublicPermissions]

    @swagger_auto_schema(manual_parameters=[page_param])
    def get(self, request, pk):
        """
        get 'id' of category <required>
        get 'page' as parameter <optional>
        return list of news by category id, pagination 20
        """
        try:
            queryset = News.objects.filter(category_id=pk)
            page = value_validator(self.request.query_params.get('page', 1))
            queryset = data_from_page(queryset, page)
            serializer = NewsListSerializer(queryset, many=True)
            data = {'code': 0, 'list': serializer.data}
            status = 200
        except Exception as err:
            data = {'code': 1, 'message': str(err)}
            status = 400
        return Response(data=data, status=status)


class CategoryListNews(APIView):
    """
    """

    permission_classes = [PublicPermissions]

    def get(self, request):
        """
        return list of all news categories, without pagination
        """
        queryset = Category.objects.all()
        try:
            serializer = CategoriesSerializer(queryset, many=True)
            data = {'code': 0, 'list': serializer.data}
            status = 200
        except Exception as err:
            data = {'code': 1, 'message': str(err)}
            status = 400
        return Response(data=data, status=status)


class NewsDetail(APIView):
    """
    get 'id' as parameter <required>
    return detail news
    """

    permission_classes = [PublicPermissions]

    @swagger_auto_schema(manual_parameters=[id_news_param])
    def get(self, request):
        """
        """
        news_id = self.request.query_params.get('id', 1)
        if value_validator_news(news_id):
            news_id = int(news_id)
        else:
            data = {'code': 1, 'message': 'incorrect id'}
            return Response(data=data, status=400)

        queryset = News.objects.filter(id=news_id)
        try:
            serializer = NewsSerializer(queryset, many=True)
            data = {'code': 0, 'news': serializer.data}
            status = 200
        except Exception as err:
            data = {'code': 1, 'message': str(err)}
            status = 400
        return Response(data=data, status=status)
