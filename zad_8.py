import argparse
import urllib
import urllib.request
import ssl
import json
import datetime


class Brawery(object):
    id: str
    name: str
    brewery_type: str
    street: str
    address_2: str
    address_3: str
    city: str
    state: str
    county_province: str
    postal_code: str
    country: str
    longitude: str
    latitude: str
    phone: str
    website_url: str
    updated_at: datetime
    created_at: datetime

    def __init__(self, id: str, name: str, brewery_type: str, street: str, address_2: str, address_3: str, city: str,
                 state: str, county_province: str, postal_code: str, country: str, longitude: str, latitude: str,
                 phone: str, website_url: str, updated_at: datetime, created_at: datetime):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return f'Brawery {self.name} in {self.city} ({self.country}) of type {self.brewery_type}'


ssl._create_default_https_context = ssl._create_unverified_context
parser = argparse.ArgumentParser()
parser.add_argument('--city', type=str, required=False, help='Pass city to display braweries located in it')
args = vars(parser.parse_args())
city = args['city']
contents: any

if city != '' and city is not None:
    contents = urllib.request.urlopen(f"https://api.openbrewerydb.org/breweries?by_city={city}").read()
else:
    contents = urllib.request.urlopen("https://api.openbrewerydb.org/breweries?page=20").read()

brawery_json = json.loads(contents, object_hook=lambda b: Brawery(**b))

for element in brawery_json:
    print(element)
