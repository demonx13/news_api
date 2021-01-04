from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view()),
    path('categories/<int:pk>/news/<int:page>', views.NewsByCategory.as_view()),
    path('categories/<int:pk>/news/', views.ListNewsRedirect),
    path('fff/', views.CategoryViewSet.as_view({'get': 'list'})),

]
