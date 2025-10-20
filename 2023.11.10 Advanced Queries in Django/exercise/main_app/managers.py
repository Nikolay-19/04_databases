from django.db import models
from django.db.models import Max, Min, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price, max_price):
        return self.filter(price__gte=min_price, price__lte=max_price)

    def with_bedrooms(self, bedrooms_count):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        locations = self.annotate(a=models.Count("location")).order_by("id")[:2]
        result = [{"location": locations[0].location}, {"location": locations[1].location}]
        return result


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre):
        return self.filter(genre=genre)

    def recently_released_games(self, year):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.annotate(max_rating=Max("rating")).order_by("-max_rating").first()

    def lowest_rated_game(self):
        return self.annotate(min_rating=Min("rating")).order_by("min_rating").first()

    def average_rating(self):
        avg = self.aggregate(avg_rt=Avg("rating"))["avg_rt"]
        return f"{avg:.1f}"
