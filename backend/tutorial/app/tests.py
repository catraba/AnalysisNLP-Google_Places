from django.test import TestCase

# Create your tests here.

import requests
import json

place_id = 'Adri'

url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key=YOUR_API_KEY'.format(place_id)

data = requests.post(url).json()

print(data['error_message'])