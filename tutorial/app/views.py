from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers, viewsets

from app.models import Place
from app.serializers import PlaceSerializer

import json
import requests
import spacy
#import es_core_news_sm
nlp = spacy.load('es_core_news_sm', disable=['ner'])

from app.analyzers.analyzer import Analyzer
from app.analyzers.text_cleaner import textCleaner
from app.analyzers.match_searcher import matchSearcher

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    """
    Este viewset automáticamente lista, crea, devuelve,
    actualiza y destruye acciones.

    Adicionalmente podemos acompañar con una acción 'highlight'.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        place = self.get_object()
        return Response(place.highlighted)


class DemoView(APIView):
    def get(self, request, format=None):
        
        data = Analyzer('../tutorial/app/analyzers/demo.json')

        return Response(data)


class DemoMatcher(APIView):
    def get(self, request, format=None):

        result = textCleaner(nlp, '../tutorial/app/analyzers/demo.json')

        data = matchSearcher(nlp, result, 'sitio')

        return Response(data)


class TestView(APIView):
    def post(self, request, format=None):
        place_id = request.data['nombre']

        url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key=YOUR_API_KEY'.format(place_id)
        data = requests.post(url).json()

        return Response(data)
