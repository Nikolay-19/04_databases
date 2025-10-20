from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from main_app.validators import validate_name, validate_phone_number


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=18,
                                                                    message="Age must be greater than 18")])
    email = models.EmailField(error_messages={"invalid": "Enter a valid email address"})
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
    website_url = models.URLField(error_messages={"invalid": "Enter a valid URL"})


def author_validator(value):
    if len(value) < 5:
        raise ValidationError("Author must be at least 5 characters long")


def isbn_validator(value):
    if len(value) < 6:
        raise ValidationError("ISBN must be at least 6 characters long")


def director_validator(value):
    if len(value) < 8:
        raise ValidationError("Director must be at least 8 characters long")


def artist_validator(value):
    if len(value) < 9:
        raise ValidationError("Artist must be at least 9 characters long")


class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]


class Book(BaseMedia):
    author = models.CharField(max_length=100, validators=[author_validator])
    isbn = models.CharField(max_length=20, unique=True, validators=[isbn_validator])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"


class Movie(BaseMedia):
    director = models.CharField(max_length=100, validators=[director_validator])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"


class Music(BaseMedia):
    artist = models.CharField(max_length=100, validators=[artist_validator])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return float(self.price) * 0.08

    @staticmethod
    def calculate_shipping_cost(weight):
        return float(weight) * 2

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return float(self.price) * 1.2

    def calculate_tax(self):
        return float(self.price) * 0.05

    @staticmethod
    def calculate_shipping_cost(weight):
        return float(weight) * 1.5

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


class RechargeEnergyMixin(models.Model):
    energy = models.PositiveIntegerField()

    def recharge_energy(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        self.save()

    class Meta:
        abstract = True


class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)


class SpiderHero(Hero):
    def swing_from_buildings(self):
        self.energy -= 80
        if self.energy <= 0:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        else:
            self.save()
            return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True


class FlashHero(Hero):
    def run_at_super_speed(self):
        self.energy -= 65
        if self.energy <= 0:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        else:
            self.save()
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True
