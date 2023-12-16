import time
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


class GeoLocator:
    half_km = 0.004501

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/120.0.0.0 Safari/537.36"

    def get_latitude_longtitude(self, address):
        geolocator = Nominatim(
            user_agent=self.user_agent)
        location = geolocator.geocode(address)
        return location.latitude, location.longitude

    def find_address_with_coords(self, coords_in_string):
        geolocator = Nominatim(
            user_agent=self.user_agent)
        location = geolocator.reverse(coords_in_string)
        print(location)
        return location

    @staticmethod
    def measure_distantion(coords1, coords2):
        print(geodesic(coords2, coords1).m, 'meters')
        distance = geodesic(coords2, coords1).meters
        return distance

    def step_to(self, coords, direction="up", multiplicator=1):
        print(f"coords was {coords}")
        long, lang = coords[0], coords[1]
        step = self.half_km * multiplicator

        if direction == "up":
            long = long + step
        if direction == "down":
            long = long - step
        if direction == "right":
            lang = lang + step
        if direction == "left":
            lang = lang - step

        new_coords = (long, lang)
        print(f"coords is {new_coords}")
        return new_coords


geo = GeoLocator()
# geo.find_address_with_coords((43.8424821, -79.02111270))
bayli_street_75 = geo.get_latitude_longtitude("75 Bayly Street West")
for i in range(100):
    up = geo.step_to((43.8424821, -79.0211127), direction="left", multiplicator=i)
    geo.measure_distantion(coords1=bayli_street_75, coords2=up)
    time.sleep(1.5)
