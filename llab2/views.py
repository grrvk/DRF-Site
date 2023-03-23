from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Transport
from .serializers import TransportSerializer


# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    #serializer = TransportSerializer(data=request.data)
    #if serializer.is_valid():
    #    print(serializer.data)
    #    data = serializer.data
    data = request.data
    serializer = TransportSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid": "bad data"}, status=400)