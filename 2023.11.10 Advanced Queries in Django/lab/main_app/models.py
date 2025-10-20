from django.db import models
from main_app.managers import ProductManager


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


def product_quantity_ordered():
    products = Product.objects.annotate(qt=models.Sum('orderproduct__quantity')).exclude(qt=None).order_by('-qt')
    result = [f"Quantity ordered of {el.name}: {el.qt}" for el in products]
    return "\n".join(el for el in result)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related("orderproduct_set__product__category")
    #       Table1.objects.prefetch_related("tableeeeeee2_set__tablee3__tableee4")
    result = []
    for i in orders:
        result.append(f"Order ID: {i.id}, Customer: {i.customer.username}")
        for j in i.orderproduct_set.all():
            result.append(f"- Product: {j.product.name}, Category: {j.product.category.name}")
    return "\n".join(str(el) for el in result)


def filter_products():
    products = Product.objects.filter(is_available=True, price__gt=3).order_by("-price", "name")
    result = [f"{el.name}: {el.price}lv." for el in products]
    return "\n".join(str(el) for el in result)


def give_discount():
    products = Product.objects.filter(is_available=True, price__gt=3)

    for product in products:
        product.price = float(product.price) * 0.7
        product.save()

    result = [f"{product.name}: {product.price:.2f}lv." for product in Product.objects.filter(is_available=True).order_by("-price", "name")]

    return "\n".join(str(el) for el in result)
