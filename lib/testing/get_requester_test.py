from GetRequester import GetRequester
import json

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

JSON_STRING = b"""[
  {
    "name": "Daniel",
    "occupation": "LG Fridge Salesman"
  },
  {
    "name": "Joe",
    "occupation": "WiFi Fixer"
  },
  {
    "name": "Avi",
    "occupation": "DJ"
  },
  {
    "name": "Howard",
    "occupation": "Mountain Legend"
  }
]"""

CONVERTED_DATA = [
    { 'name': 'Daniel', 'occupation': 'LG Fridge Salesman' },
    { 'name': 'Joe', 'occupation': 'WiFi Fixer' },
    { 'name': 'Avi', 'occupation': 'DJ' },
    { 'name': 'Howard', 'occupation': 'Mountain Legend' }
]

def test_get_response():
    '''get_response_body function returns correct raw data.'''
    requester = GetRequester(URL)
    assert json.loads(requester.get_response_body()) == json.loads(JSON_STRING)

def test_load_json():
    '''load_json function returns parsed JSON data.'''
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
