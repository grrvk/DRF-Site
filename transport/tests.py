from rest_framework.test import APITestCase, APIRequestFactory

from .models import Transport
from .views import TransportListCreateView, TransportDetailApiView, TransportUpdateApiView, TransportDestroyApiView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from llab2.models import Route, City, Country

User = get_user_model()

def create_route():
    sample_country = Country.objects.create(name='test_country')
    sample_city_1 = City.objects.create(name='test_city_1', country=sample_country)
    sample_city_2 = City.objects.create(name='test_city_2', country=sample_country)
    sample_route = Route.objects.create(
        number="1",
    )
    sample_route.cities.add(sample_city_1)
    sample_route.cities.add(sample_city_2)
    return sample_route

# Create your tests here.
class TransportListCreateTestCase(APITestCase):
    def setUp(self):

        self.factory = APIRequestFactory()
        self.view = TransportListCreateView.as_view()
        self.url = reverse('transport-list')
        self.user = User.objects.create_superuser(
            username="vika",
            email="test@gmail.com",
            password="admin",
        )

    def test_transport_list(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transport_post(self):
        sample_transport = {
            "route": create_route().id,
            "type": "Train",
            "number": "171",
            "num_of_passengers": "200"
        }
        request = self.factory.post(self.url, sample_transport)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TransportDetailsTestCase(APITestCase):
    def setUp(self):
        self.sample_transport = Transport.objects.create(
            route=create_route(),
            type="Train",
            number="171",
            num_of_passengers="200",
        )

        self.factory = APIRequestFactory()
        self.view = TransportDetailApiView.as_view()
        self.url = reverse('transport-detail', kwargs={'pk': self.sample_transport.pk})
        self.user = User.objects.create_superuser(
            username="vika",
            email="test@gmail.com",
            password="admin",
        )

    def test_transport_details_get(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = self.view(request, pk=self.sample_transport.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TransportDetailUpdateTestCase(APITestCase):
    def setUp(self):
        self.sample_transport = Transport.objects.create(
            route=create_route(),
            type="Train",
            number="171",
            num_of_passengers="200",
        )

        self.factory = APIRequestFactory()
        self.view = TransportUpdateApiView.as_view()
        self.url = reverse('transport-edit', kwargs={'pk': self.sample_transport.pk})
        self.user = User.objects.create_superuser(
            username="vika",
            email="test@gmail.com",
            password="admin",
        )

    def test_transport_details_update(self):
        request = self.factory.patch(self.url, {
            'number': "171",
            'num_of_passengers': "200",
        })
        request.user = self.user
        response = self.view(request, pk=self.sample_transport.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TransportDetailDeleteTestCase(APITestCase):
    def setUp(self):
        self.sample_transport = Transport.objects.create(
            route=create_route(),
            type="Train",
            number="171",
            num_of_passengers="200",
        )

        self.factory = APIRequestFactory()
        self.view = TransportDestroyApiView.as_view()
        self.url = reverse('transport-delete', kwargs={'pk': self.sample_transport.pk})
        self.user = User.objects.create_superuser(
            username="vika",
            email="test@gmail.com",
            password="admin",
        )

    def test_transport_details_delete(self):
        request = self.factory.delete(self.url)
        request.user = self.user
        response = self.view(request, pk=self.sample_transport.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
