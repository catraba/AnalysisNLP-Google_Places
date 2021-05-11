from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Consumer
from .permissions import IsOwner
from .serializers import UserSerializer, ConsumerSerializer

import requests
import json

# Create your views here.


class UserList(APIView):
    '''
    Devuelve los usuarios registrados y/o crea uno nuevo
    '''

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumerList(APIView):
    '''
    Devuelve los usuarios con la API_KEY configurada o
    registra a los que no la tengan
    '''

    permission_classes = [IsAuthenticated]

    def get(self, request):
        consumer = Consumer.objects.all()
        serializer = ConsumerSerializer(consumer, many=True)
        
        return Response(serializer.data)

        
    def post(self, request):
        serializer = ConsumerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumerDetail(APIView):
    '''
    Devuelve, actualiza o elimina un consumer en particular
    '''

    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            return Consumer.objects.get(pk=pk)
        except:
            raise Http404

    
    def get(self, request, pk):
        consumer = self.get_object(pk)
        serializer = ConsumerSerializer(consumer)

        return Response(serializer.data)


    def put(self, request, pk):
        consumer = self.get_object(pk)
        serializer = ConsumerSerializer(consumer, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        consumer = self.get_object(pk)
        consumer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AnalyzerResponse(APIView):
    '''
    Realiza el request a Google Places API
    '''

    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            return Consumer.objects.get(pk=pk)
        except:
            raise Http404

    def post(self, request, pk):
        consumer = self.get_object(pk=pk)
        serializer = ConsumerSerializer(consumer)

        api_key = serializer.data['api_key']

        try:
            place_id = request.data['place_id']

            url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key={}'.format(place_id, api_key)
            data = requests.post(url).json()

            if data['error_message']:
                return Response(data)

        except:
            return Response('No place_id provided', status=status.HTTP_400_BAD_REQUEST)
