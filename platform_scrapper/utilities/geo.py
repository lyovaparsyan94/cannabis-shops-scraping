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
        print(f"{address} latitude: {location.latitude}, longtitude: {location.longitude}")
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

    def get_radius_area(self):
        ...

    def get_square(self):
        ...


geo = GeoLocator()
# geo.find_address_with_coords((43.8424821, -79.02111270))
yerevan = geo.get_latitude_longtitude(address="Yerevan armenia")
geo.step_from(yerevan, direction="left", multiplicator=40)