import time
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pprint import pprint
import pprint
from platform_scrapper.configs.constants import HEADERS

class GeoLocator:
    half_km = 0.004501

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/120.0.0.0 Safari/537.36"
        self.geolocator = Nominatim(user_agent=self.user_agent)

    def get_latitude_longtitude(self, address):
        location = self.geolocator.geocode(address)
        # print(f"{address} latitude: {location.latitude}, longtitude: {location.longitude}")
        return location.latitude, location.longitude

    def get_city_state_zipcode_lat_long(self, address):
        location = self.geolocator.reverse(address)
        _lat = location.raw['lat']
        _lon = location.raw['lon']
        _city = location.raw['address'].get('city', None)
        _postcode = location.raw['address'].get('postcode')
        _state = location.raw['address']['state']
        return _city, _postcode, _state, _lat, _lon

    def find_address_with_coords(self, coords):
        geolocator = Nominatim(
            user_agent=self.user_agent)
        location = geolocator.reverse(coords)
        return location

    @staticmethod
    def measure_distantion(coords1, coords2):
        print(f"Distance is {int(geodesic(coords2, coords1).m)} meters")
        distance = geodesic(coords2, coords1).meters
        return distance

    def step_from(self, coords, direction="up", multiplicator=1, step=half_km):
        print(f"initial coords was {coords}")
        long, lang = coords[0], coords[1]
        if multiplicator != 0:
            step = step * multiplicator

        if direction == "up":
            long = long + step
        if direction == "down":
            long = long - step
        if direction == "right":
            lang = lang + step
        if direction == "left":
            lang = lang - step
        if direction == "upleft":
            long = long + step
            lang = lang - step
        if direction == "upright":
            long = long + step
            lang = lang + step
        if direction == "leftdown":
            long = long - step
            lang = lang - step
        if direction == "rightdown":
            lang = lang + step
            long = long - step

        new_coords = (long, lang)
        print(f"New coords after movement are {new_coords}")
        return new_coords


def test():
    geo = GeoLocator()
    # 1 get long lang from current address
    # bayly = geo.get_latitude_longtitude("Lake Ontario canada")
    bayly = geo.get_latitude_longtitude("75 Bayly St ajax canada")


    # 2 move to right 0.5km, get new address, measure distantion and make graphql query
    new_addres = geo.step_from(bayly, direction="right", multiplicator=1)
    # geo.measure_distantion(bayly, new_address)
    new_addres_location = geo.get_city_state_zipcode_lat_long(new_addres)
    # 3 check delivery with new address
    dispensaryId = "tweed-ajax"
    # dispensaryId = "pluto-plants-etobicoke"
    # dispensaryId = "budssmoke-st-catharines"
    # dispensaryId = "lolly-pickering"
    # dispensaryId = "lolly-pickering"
    # dispensaryId = "star-buds-canmore"
    hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"

    city, state, zipcode, lat, lng = new_addres_location
    print(new_addres_location)
    # url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
    url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{''}%22%2C%22state%22%3A%22{''}%22%2C%22zipcode%22%3A%22%20{''}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
    # # url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables=%7B%22dispensaryFilter%22%3A%7B%22cNameOrID%22%3A%226126c36e566a61009c2b3090%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22%7D%7D"
    cons_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"tweed-ajax"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}'
    print(url)
    # print(cons_url)
    res = requests.get(url=url, headers=HEADERS)
    cons_url = requests.get(url=cons_url, headers=HEADERS)
    # res1 = requests.get(url=cons_url, headers=headers)

    pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])
    withbounds = True
    if withbounds:
        pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo']['withinBounds'])
        pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])
    # pprint.pprint(res.json())
    else:
        pprint.pprint(cons_url.json()['data']['filteredDispensaries'][0]['enabledOrderTypes'])

# test()
# for i in range(10):
#     time.sleep(10)
#     test()
from geopy import Point
from geopy.distance import distance

# Define the two points
point1 = Point(43.8424821, -78.9265917)
point2 = Point(point1.latitude - 1, point1.longitude - 1)

# Calculate the bearing between the two points
bearing = distance(point1, point2).bearing

# Add 10 degrees to the calculated bearing to get the direction to the northwest at 10 degrees
nw_bearing = (bearing - 10) % 360

# Print the direction to the northwest at 10 degrees
print(f"The direction from ({point1.latitude}, {point1.longitude}) to the northwest at 10 degrees is N {nw_bearing:.1f}° W.")