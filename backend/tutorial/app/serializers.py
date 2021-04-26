from rest_framework import serializers

from app.models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='place-highlight', format='html')

    class Meta:
        model = Place
        fields = ['id', 'title', 'url', 'highlight']
