import time
import requests
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pprint import pprint
from global_land_mask import globe
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

    def get_city_state_zipcode_lat_long(self, address, retry=10, interval=1):
        time.sleep(1)
        response = None
        while not response and retry >= 1:
            try:
                time.sleep(interval)
                # location = self.get_latitude_longtitude(address)
                location = self.geolocator.reverse(address, timeout=None)
                print(location.raw.get('type'), "No type")
                _lat = location.raw['lat']
                _lon = location.raw['lon']
                _city = location.raw['address'].get('city', None)
                _postcode = location.raw['address'].get('postcode')
                _state = location.raw['address'].get('state')
                print(f"City={_city}, postocode={_postcode}, state={_state}")
                response = _city, _postcode, _state, _lat, _lon
                return response
            except Exception as e:
                retry -= 1
                interval += 1
                print(f"retry is {retry}, interval - {interval}")
        return response

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


geo = GeoLocator()
# 1 get long lang from current address
# bayly = geo.get_city_state_zipcode_lat_long("75 Bayly St ajax canada")

# bayly = geo.get_city_state_zipcode_lat_long((43.263961505251174, -79.81651655067857)) #city
# time.sleep(5)
# bayly1 = geo.get_city_state_zipcode_lat_long((43.614215254585226, -78.70471115595248)) #lake
# time.sleep(5)
# bayly2 = geo.get_city_state_zipcode_lat_long((43.23529374678142, -79.50283896985108)) #lake
# time.sleep(5)
# bayly3 = geo.get_city_state_zipcode_lat_long((43.715033659941525, -78.36072606089238)) #lake
#
#
#     # 2 move to right 0.5km, get new address, measure distantion and make graphql query
#     new_addres = geo.step_from(bayly, direction="right", multiplicator=1)
#     # geo.measure_distantion(bayly, new_address)
#     new_addres_location = geo.get_city_state_zipcode_lat_long(new_addres)
#     # 3 check delivery with new address
#     dispensaryId = "tweed-ajax"
#     # dispensaryId = "pluto-plants-etobicoke"
#     # dispensaryId = "budssmoke-st-catharines"
#     # dispensaryId = "lolly-pickering"
#     # dispensaryId = "lolly-pickering"
#     # dispensaryId = "star-buds-canmore"
#     hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"
#
#     city, state, zipcode, lat, lng = new_addres_location
#     print(new_addres_location)
#     # url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
#     url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{''}%22%2C%22state%22%3A%22{''}%22%2C%22zipcode%22%3A%22%20{''}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
#     # # url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables=%7B%22dispensaryFilter%22%3A%7B%22cNameOrID%22%3A%226126c36e566a61009c2b3090%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22%7D%7D"
#     cons_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"tweed-ajax"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}'
#     print(url)
#     # print(cons_url)
#     res = requests.get(url=url, headers=HEADERS)
#     cons_url = requests.get(url=cons_url, headers=HEADERS)
#     # res1 = requests.get(url=cons_url, headers=headers)
#
#     pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])
#     withbounds = True
#     if withbounds:
#         pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo']['withinBounds'])
#         pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])
#     # pprint.pprint(res.json())
#     else:
#         pprint.pprint(cons_url.json()['data']['filteredDispensaries'][0]['enabledOrderTypes'])
#
# # for i in range(10):
# #     time.sleep(10)
# #     test()
