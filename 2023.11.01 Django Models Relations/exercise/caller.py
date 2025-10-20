import datetime
import os
import django
from datetime import date, timedelta

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create queries within functions
from main_app.models import (Author, Book, Song, Artist, Product, Review, Driver, DrivingLicense, Car, Owner,
                             Registration)


def show_all_authors_with_their_books():
    authors = Author.objects.order_by("id")
    result = []

    for author in authors:
        books_temp = Book.objects.filter(author_id=author.id)
        books = [el.title for el in books_temp]
        if not books:
            continue
        result.append(f"{author.name} has written - {', '.join(books)}!")

    return "\n".join(str(el) for el in result)


def delete_all_authors_without_books():
    for author in Author.objects.all():
        if not Book.objects.filter(author_id=author.id):
            author.delete()

# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
# book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", price=19.99, author=author1)
# book2 = Book.objects.create(title="1984", price=14.99, author=author2)
# book3 = Book.objects.create(title="To Kill a Mockingbird", price=12.99, author=author3)
# book4 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", price=19.99, author=author1)
# print(show_all_authors_with_their_books())
# delete_all_authors_without_books()
# print(Author.objects.count())


def add_song_to_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song2 = Song.objects.get(title=song_title)
    artist.songs.add(song2)


def get_songs_by_artist(artist_name):
    artist = Artist.objects.get(name=artist_name)
    return Song.objects.filter(id=artist.id).order_by("-id")


def remove_song_from_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song3 = Song.objects.get(title=song_title)
    artist.songs.remove(song3)

# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


def calculate_average_rating_for_product_by_name(product_name):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    total = sum(r.rating for r in reviews)
    average_rating = total / len(reviews)

    return average_rating


def get_reviews_with_high_ratings(threshold):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")
    # return [el for el in Product.objects.all().order_by("-name") if not Review.objects.filter(product_id=el.id)]


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()

# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
# print(calculate_average_rating_for_product_by_name("Laptop"))


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by("-license_number")
    result = []
    for lic in licenses:
        expiration = lic.issue_date + timedelta(days=365)
        result.append(f"License with id: {lic.license_number} expires on {expiration}!")

    return "\n".join(str(el) for el in result)


def get_drivers_with_expired_licenses(due_date):
    drivers = Driver.objects.all()
    licenses = DrivingLicense.objects.all()
    result = []
    for lic in licenses:
        if lic.issue_date + timedelta(days=365) >= due_date + timedelta(days=1):
            result.append(Driver.objects.get(id=lic.driver_id))

    return result

# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")


def register_car_by_owner(owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()
    car.owner = owner
    car.registration = registration
    car.save()
    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} with registration number "
            f"{registration.registration_number}.")

# owner1 = Owner.objects.create(name='Ivelin11 Milchev')
# owner2 = Owner.objects.create(name='Alice11 Smith')
# car1 = Car.objects.create(model='Citroen11 C5', year=2004)
# car2 = Car.objects.create(model='Honda11 Civic', year=2021)
# registration1 = Registration.objects.create(registration_number='TX1110044XA')
# registration2 = Registration.objects.create(registration_number='XY11Z789')
# print(register_car_by_owner(owner1))
