from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


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

    @property
    def property_should_index(self):
        return True


class City(models.Model):
    name = models.CharField(max_length=250, unique=True, validators=[validate_name])
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

    @property
    def property_should_index(self):
        return True


def validate_number(value):
    for char in value:
        if not char.isnumeric():
            raise ValidationError("Invalid number format")
    if int(value) < 1:
        raise ValidationError("Invalid number format. Number must be more than 0")


class Route(models.Model):
    number = models.CharField(max_length=20, unique=True, validators=[validate_number])
    cities = models.ManyToManyField(City, related_name='cities')

    def __str__(self):
        if self.cities.count() > 2:
            return self.number + ': ' + self.cities.all().first().name + ' - ... - ' + self.cities.all().last().name
        return self.number + ': ' + self.cities.all().first().name + ' - ' + self.cities.all().last().name

    def city_names(self):
        return [str(city) for city in self.cities.all()]
