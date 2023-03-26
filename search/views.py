from rest_framework import generics
from rest_framework.response import Response
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        result = client.perform_search(query, tags=tag)
        return Response(result)

