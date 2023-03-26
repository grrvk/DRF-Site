from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Transport
from llab2.models import City, Route


@register(Transport)
class TransportIndex(AlgoliaIndex):
    fields = [
        'route',
        'type',
        'number',
        'num_of_passengers',
    ]
    tags = 'get_tags_list'


@register(Route)
class RouteIndex(AlgoliaIndex):
    fields = [
        'number',
        'city_names',
    ]


@register(City)
class CityIndex(AlgoliaIndex):
    fields = [
        'name',
        'country',
    ]
