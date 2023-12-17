import time
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pprint import pprint
import pprint


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
        _city = location.raw['address']['city']
        _postcode = location.raw['address']['postcode']
        _state = location.raw['address']['state']
        return _city, _postcode, _state, _lat, _lon

    def find_address_with_coords(self, coords):
        geolocator = Nominatim(
            user_agent=self.user_agent)
        location = geolocator.reverse(coords)
        return location

    @staticmethod
    def measure_distantion(coords1, coords2):
        print(f"Distation after movement is {int(geodesic(coords2, coords1).m)} meters")
        distance = geodesic(coords2, coords1).meters
        return distance

    def step_from(self, coords, direction="up", multiplicator=1, step=half_km*2):
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


geo = GeoLocator()
# 1 get long lang from current address
bayly = geo.get_latitude_longtitude("715 Krosno Blvd Pickering, ON")
# 2 move to right 0.5km, get new address, measure distantion and make graphql query
new_address = geo.step_from(bayly, direction="upright", multiplicator=1)
geo.measure_distantion(bayly, new_address)
new_addres_location = geo.get_city_state_zipcode_lat_long(new_address)
# 3 check delivery with new address
dispensaryId = "tweed-ajax"
# dispensaryId = "pluto-plants-etobicoke"
# dispensaryId = "budssmoke-st-catharines"
# dispensaryId = "lolly-pickering"
# dispensaryId = "lolly-pickering"
# dispensaryId = "star-buds-canmore"

hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"

city, state, zipcode, lat, lng = new_addres_location
url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
# url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables=%7B%22dispensaryFilter%22%3A%7B%22cNameOrID%22%3A%226126c36e566a61009c2b3090%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22%7D%7D"
cons_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"tweed-ajax"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Cookie": "_ga_1QQ3EPGGJ3=GS1.1.1702054947.1.1.1702055577.60.0.0; _ga_4TSZ0LK22W=GS1.1.1702150075.2.0.1702150153.60.0.0; _ga_7F3HGF7PL4=GS1.1.1702480932.1.1.1702481847.60.0.0; _ga_5CCKH1MX6Y=GS1.1.1702649940.1.0.1702649960.40.0.0; _gid=GA1.2.1433509371.1702809491; __cflb=04dToaXWHAPESU8RyBQBc8Yta2dmM5dTc3JC5ZvpMD; _gat=1; _gat_UA-101536475-5=1; _ga=GA1.2.1605833789.1702809491; _ga_FZN7LD29Z4=GS1.1.1702813263.2.1.1702817191.0.0.0"
}

res = requests.get(url=url, headers=headers)
res1 = requests.get(url=cons_url, headers=headers)
pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])
pprint.pprint(res1.json())
