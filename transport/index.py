from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Transport

@register(Transport)
class TransportIndex(AlgoliaIndex):
    fields = [
        'route',
        'type',
        'number',
        'num_of_passengers',
    ]
    tags = 'get_tags_list'
