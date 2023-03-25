from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Transport
from .serializers import TransportSerializer
from llab2.mixins import StaffEditorPermissionMixin


class TransportDetailApiView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    # lookup_field = 'pk'


class TransportListCreateView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        route = serializer.validated_data.get('route')
        serializer.save()


class TransportUpdateApiView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def perform_update(self, serializer):
        instance = serializer.save()


class TransportDestroyApiView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class TransportListApiView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    # lookup_field = 'pk'


@api_view(['GET', 'POST'])
def transport_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Transport, pk=pk)
            data = TransportSerializer(obj, many=False).data
            return Response(data)
        qs = Transport.objects.all()
        data = TransportSerializer(qs, many=True).data
        return Response(data)
    if method == "POST":
        serializer = TransportSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)
        return Response({"invalid": "bad data"}, status=400)
