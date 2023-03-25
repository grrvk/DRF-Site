from rest_framework import serializers
from rest_framework.reverse import reverse

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

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("transport-edit", kwargs={"pk": obj.pk}, request=request)
