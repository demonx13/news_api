from django.core.management.base import BaseCommand
from src.news.models import News, Category
from .news_fake_data import newsdata
from django.contrib.auth.models import User


class Command(BaseCommand):
    """command to create db elements for test workability
    """
    def handle(self, *args, **options):
        self.create_category()
        self.create_news()
        self.stdout.write("Success")

    def create_category(self):
        """
        """
        ctg = Category.objects.all()
        if ctg and len(ctg) > 10:
            print('Categories already exist')
        else:
            for i in range(20):
                Category.objects.create(
                    name=f"test_category_{i+1}",
                )

    def create_news(self):
        """
        """
        nws = News.objects.all()
        if nws and len(nws) > 50:
            print("News already exist")
        else:
            counter = 0
            user = User.objects.all()[0]
            category_list = Category.objects.all()
            for category in category_list:
                # print(category)
                for i in range(20):
                    counter += 1
                    News.objects.create(
                        category=category,
                        writer=user,
                        full_description=newsdata.get('full_description'),
                        short_description=newsdata.get('short_description'),
                        title=f"{newsdata.get('title')} #{counter}",
                        visible=True
                    )
