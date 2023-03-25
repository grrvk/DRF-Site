from django.shortcuts import render
from rest_framework import generics
from transport.models import Transport
from transport.serializers import TransportSerializer
from rest_framework.response import Response
from . import client


# Create your views here.
class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        result = client.perform_search(query, tags=tag)
        return Response(result)


class SearchListOldView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        result = Transport.objects.none()
        if q is not None:
            result = qs.search(q)
        return result
