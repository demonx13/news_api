from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListNews.as_view()),
    path('categories/<int:pk>/news/', views.NewsByCategory.as_view()),
    path('details/', views.NewsDetail.as_view())
]
