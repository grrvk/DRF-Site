from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

def validate_name(value):
    for char in value:
        if not (char.isalpha() or char == ' '):
            raise ValidationError("Invalid name format")


class Country(models.Model):
    name = models.CharField(max_length=250, unique=True, validators=[validate_name])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField(max_length=250, unique=True, validators=[validate_name])
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


def validate_number(value):
    for char in value:
        if not char.isnumeric():
            raise ValidationError("Invalid number format")


class Route(models.Model):
    number = models.CharField(max_length=20, unique=True, validators=[validate_number])
    cities = models.ManyToManyField(City, related_name='cities')

    def __str__(self):
        return self.number + ': ' + self.cities.all().first().name + ' - ' + self.cities.all().last().name


class Transport(models.Model):
    TRANSPORT_TYPES = (
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Plane', 'Plane'),
    )
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True,
                              related_name='route')
    type = models.CharField(choices=TRANSPORT_TYPES, max_length=10, default='no type')
    number = models.CharField(max_length=10, unique=True, validators=[validate_number])
    num_of_passengers = models.CharField(max_length=10, validators=[validate_number], blank=True)

    def __str__(self):
        return self.type + ' ' + self.number
