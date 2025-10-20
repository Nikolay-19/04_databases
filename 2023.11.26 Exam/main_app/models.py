from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import Count


# Create your models here.
class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(num_articles=Count("articles_authors")).order_by("-num_articles", "email")


class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2005)])
    website = models.URLField(blank=True, null=True)
    objects = AuthorManager()


class Article(models.Model):
    CATS = (("Technology", "Technology"), ("Science", "Science"), ("Education", "Education"))
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    content = models.TextField(validators=[MinLengthValidator(10)])
    category = models.CharField(max_length=10, default="Technology", choices=CATS)
    authors = models.ManyToManyField(Author)
    published_on = models.DateTimeField(auto_now_add=True, editable=False)


class Review(models.Model):
    content = models.TextField(validators=[MinLengthValidator(10)])
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="reviews_authors")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reviews_articles")
    published_on = models.DateTimeField(auto_now_add=True, editable=False)
