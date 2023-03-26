from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    return Response({"url": "http://127.0.0.1:8000/home/"})


def home_view(request):
    return render(request, 'main/home.html')


def transport_search_view(request):
    return render(request, 'search/transport_search.html')


def routes_search_view(request):
    return render(request, 'search/route_search.html')


def cities_search_view(request):
    return render(request, 'search/city_search.html')