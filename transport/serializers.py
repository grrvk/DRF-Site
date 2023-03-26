from rest_framework import serializers
from .models import Transport


class TransportSerializer(serializers.ModelSerializer):
    # edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='transport-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Transport
        fields = [
            'url',
            'pk',
            'route',
            'type',
            'number',
            'num_of_passengers',
        ]
