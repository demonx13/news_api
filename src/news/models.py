from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Category of news
    """
    themes = models.CharField("Themes", max_length=50,)

    def __str__(self):
        return self.themes

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class News(models.Model):
    """News model
    """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    fullDescription = models.TextField("News detail ", max_length=1000)
    shortDescription = models.TextField('Short description', max_length=200, default="")
    title = models.CharField("News title", max_length=100)
    visible = models.BooleanField("Published", default=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"

    def __str__(self):
        return f"{self.id} / {self.title}"
