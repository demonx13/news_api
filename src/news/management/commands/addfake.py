from django.core.management.base import BaseCommand
from src.news.models import News, Category
from .news_fake_data import newsdata
from django.contrib.auth.models import User


class Command(BaseCommand):
    """command to create db elements for test workability
    """
    def handle(self, *args, **options):
        # self.create_category()
        self.create_news()
        self.stdout.write("Success")

    def create_category(self):
        for i in range(20):
            category = Category.objects.create(
                themes=f"test_category_{i}",
            )

    def create_news(self):
        user = User.objects.all()[0]

        category_list = Category.objects.all()
        for category in category_list:
            print(category)
            for i in range(20):
                News.objects.create(
                    category=category,
                    writer=user,
                    fullDescription=newsdata.get('fullDescription'),
                    shortDescription=newsdata.get('shortDescription'),
                    title=newsdata.get('title'),
                    visible=True
                )
