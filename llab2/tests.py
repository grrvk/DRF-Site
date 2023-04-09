from algoliasearch_django import AlgoliaEngine
from rest_framework.test import APITestCase
from .models import Country, City, Route


# Create your tests here.
class ObjectsCreateTestCase(APITestCase):
    def setUp(self):
        self.sample_country = Country.objects.create(name='test_country')
        self.sample_city_1 = City.objects.create(name='test_city_1', country=self.sample_country)
        self.sample_city_2 = City.objects.create(name='test_city_2', country=self.sample_country)


    def test_create_country(self):
        Country.objects.create(name="Test_country")

    def test_create_city(self):
        City.objects.create(name="Test_city", country=self.sample_country)

    def test_create_route(self):
        sample_route = Route.objects.create(
            number="1",
        )
        sample_route.cities.add(self.sample_city_1)
        sample_route.cities.add(self.sample_city_2)
