import random
import gevent
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from configs.constants import USER_AGENT


class GeoLocator:
    half_km = 0.004501

    def __init__(self):
        self.user_agent = USER_AGENT
        self.geolocator = Nominatim(user_agent=self.user_agent)

    def get_latitude_longtitude(self, address=None, store=None, state=None):
        location = None
        retry = 0
        query = [f"{' '.join(address.split()[:3])} {state} Canada",
                 f"{' '.join(address.split()[:2])} {state} Canada",
                 f" {state} {address} Canada",
                 f"Canada {address} ", f"Canada {store} {address} ",
                 f"{address} Canada {state} {store}"]
        while not location and retry <= 5:
            try:
                print(f"trying with {query[retry]}")
                location = self.geolocator.geocode(query[retry], timeout=30)
                print(f"COMAPARE address and coords - {address} vs {location.latitude} {location.longitude}")
            except Exception:
                retry += 1
        return location.latitude, location.longitude

    def get_city_state_zipcode_lat_long(self, address, retry=20, interval=1):
        gevent.sleep(random.randint(2, 7))
        response = None
        while not response and retry >= 1:
            try:
                # gevent.sleep(2)
                location = self.geolocator.reverse(address, timeout=12)
                _lat = location.raw['lat']
                _lon = location.raw['lon']
                _city = location.raw['address'].get('city', None)
                _postcode = location.raw['address'].get('postcode')
                _state = location.raw['address'].get('state')
                response = _city, _postcode, _state, _lat, _lon
                return response
            except Exception as e:
                retry -= 1
                interval += 1
                gevent.sleep(interval)
                print(f"retry is {retry}, interval - {interval}\n{e}")
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

