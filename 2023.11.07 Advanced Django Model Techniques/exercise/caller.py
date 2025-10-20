import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create queries within functions
from decimal import *
from django.core.exceptions import ValidationError
from main_app.models import (Customer, BaseMedia, Book, Movie, Music, Product, DiscountedProduct, RechargeEnergyMixin,
                             Hero, SpiderHero, FlashHero)

# customer = Customer(name="Svetlin Nakov1", age=1, email="nakov@example", phone_number="+35912345678",
#                     website_url="htsatps://nakov.com/")
# try:
#     customer.full_clean()
#     customer.save()
# except ValidationError as e:
#     print('\n'.join(e.messages))


# book = Book(title="Short Title", description="A book with a short title.", genre="Fiction", author="A", isbn="1234")
# try:
#     book.full_clean()
#     book.save()
# except ValidationError as e:
#     print("Validation Error for Book:")
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")


# product = Product.objects.create(name="Gaming Keyboard", price=Decimal(100.00))
# tax_price = product.calculate_tax()
# print(f"Tax for {product.name}: ${tax_price:.2f}")
# shipping_cost = product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {product.name}: ${shipping_cost:.2f}")
# formatted_name = product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")
# discounted_product = DiscountedProduct.objects.create(name="Gaming Mouse", price=Decimal(120.00))
# discounted_price = discounted_product.calculate_price_without_discount()
# print(f"Price Without Discount for {discounted_product.name}: ${discounted_price:.2f}")
# tax_price = discounted_product.calculate_tax()
# print(f"Tax for {discounted_product.name}: ${tax_price:.2f}")
# shipping_cost = discounted_product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {discounted_product.name}: ${shipping_cost:.2f}")
# formatted_name = discounted_product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")


# spiderman = SpiderHero(name="Spider-Man", hero_title="Spider Hero", energy=100)
# flash = FlashHero(name="The Flash", hero_title="Flash Hero", energy=70)
# spiderman.save()
# flash.save()
# print(spiderman.swing_from_buildings())
# print(flash.run_at_super_speed())
# print(spiderman.swing_from_buildings())
# spiderman.recharge_energy(195)
# flash.recharge_energy(40)
# print(f"{spiderman.name} - Energy: {spiderman.energy}")
# print(f"{flash.name} - Energy: {flash.energy}")
