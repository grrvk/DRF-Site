from rest_framework import generics
from .models import Transport
from .serializers import TransportSerializer
from llab2.mixins import StaffEditorPermissionMixin


class TransportDetailApiView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'pk'


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

