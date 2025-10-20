import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from django.db.models import Q, Count, Avg
from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    query = Q()
    if not search_name and not search_email:
        return ""
    elif search_name and search_email:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name and not search_email:
        query = Q(full_name__icontains=search_name)
    elif search_email and not search_name:
        query = Q(email__icontains=search_email)
    authors = Author.objects.filter(query).order_by("-full_name")
    if not authors:
        return ""
    result = []
    for el in authors:
        if el.is_banned:
            status = "Banned"
        else:
            status = "Not Banned"
        result.append(f"Author: {el.full_name}, email: {el.email}, status: {status}")
    return "\n".join(str(el) for el in result)


def get_top_publisher():
    author = Author.objects.get_authors_by_article_count().first()
    if not Article.objects.all():
        return ""
    return f"Top Author: {author.full_name} with {author.num_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(num_reviews=Count("reviews_authors")).order_by("-num_reviews", "email").first()
    if not Review.objects.all():
        return ""
    return f"Top Reviewer: {author.full_name} with {author.num_reviews} published reviews."


def get_top_rated_article():
    article = (Article.objects.
               annotate(num_reviews=Count("reviews_articles"), avg_rating=Avg("reviews_articles__rating")).
               filter(num_reviews__gt=0).
               order_by("-avg_rating", "title").
               first())

    if not Review.objects.all():
        return ""

    return (f"The top-rated article is: {article.title}, with an average rating of {article.avg_rating:.2f}, reviewed "
            f"{article.num_reviews} times.")


def ban_author(email=None):
    if not email:
        "No authors banned."
    author = Author.objects.filter(email__exact=email).first()
    if not author or not Author.objects.all():
        return "No authors banned."
    author.is_banned = True
    author.save()
    num_reviews = len(author.reviews_authors.all())
    reviews = author.reviews_authors.all()
    for r in reviews:
        r.delete()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."


def get_latest_article():
    if not Article.objects.all():
        return ""

    article = (Article.objects.
               prefetch_related("reviews_articles").
               filter(reviews_articles__isnull=False).
               annotate(num_reviews=Count("reviews_articles__id")).
               filter(num_reviews__gte=1).
               latest("published_on"))
    avg_review = Article.objects.filter(id=article.id).aggregate(a=Avg("reviews_articles__rating"))["a"]
    if not article:
        return ""

    authors = ", ".join(str(el.full_name) for el in article.authors.order_by("full_name").all())
    result = (f"The latest article is: {article.title}. Authors: {authors}. Reviewed: {article.num_reviews} times. "
              f"Average Rating: {avg_review:.2f}.")

    return result


print(get_latest_article())
