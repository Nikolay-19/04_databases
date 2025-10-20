from django.db import models


# Create your models here.
class Qwerty(models.Model):
    pass


class Qwerty2(models.Model):
    alive = models.BooleanField(default=False)
