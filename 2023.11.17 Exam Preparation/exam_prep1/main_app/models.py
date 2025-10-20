from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
# Create your models here.


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(count_movies=models.Count("movie__director")).order_by("-count_movies", "full_name")


class Director(models.Model):
    full_name = models.CharField(max_length=200, validators=[MinLengthValidator(limit_value=2), MaxLengthValidator(120)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=200, default="Unknown", validators=[MaxLengthValidator(50)])
    years_of_experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    objects = DirectorManager()


class Actor(models.Model):
    full_name = models.CharField(max_length=200, validators=[MinLengthValidator(limit_value=2), MaxLengthValidator(120)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=200, default="Unknown", validators=[MaxLengthValidator(50)])
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    genres = (("Action", "Action"), ("Comedy", "Comedy"), ("Drama", "Drama"), ("Other", "Other"))
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5), MaxLengthValidator(150)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=200, validators=[MaxLengthValidator(6)], default="Other", choices=genres)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)
    starring_actor = models.ForeignKey(to=Actor, on_delete=models.SET_NULL, null=True, related_name="starring_actor")
    actors = models.ManyToManyField(to=Actor, related_name="actors")
