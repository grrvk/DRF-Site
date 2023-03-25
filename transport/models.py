from django.db import models
from django.db.models import Q
import random

from llab2.models import Route, validate_number

TYPES = ['Bus', 'Train', 'Plane']


class TransportQuerySet(models.QuerySet):
    def search(self, query):
        lookup = Q(route__number__icontains=query)
        qs = self.filter(lookup)
        return qs


class TransportManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TransportQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class Transport(models.Model):
    TRANSPORT_TYPES = (
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Plane', 'Plane'),
    )
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True,
                              related_name='route')
    type = models.CharField(choices=TRANSPORT_TYPES, max_length=10, default='Bus')
    number = models.CharField(max_length=10, unique=True, validators=[validate_number])
    num_of_passengers = models.CharField(max_length=10, validators=[validate_number], blank=True)

    objects = TransportManager()

    def get_tags_list(self):
        return [random.choice(TYPES)]

    def __str__(self):
        return self.type + ' ' + self.number
