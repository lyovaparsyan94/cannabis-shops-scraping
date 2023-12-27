from gevent import monkey
# monkey.patch_all()
import json
import pprint
import time
import gevent
import requests
from data_collector import clean_data_and_save
# from queue import Queue
from geo import GeoLocator
from gevent.queue import Queue
from geopy.distance import distance
from platform_scrapper.helpers.file_handler import load_xlsx
from platform_scrapper.configs.constants import HEADERS


class ScanDutchieDelivery:
    half_km = GeoLocator.half_km
    step = 0.4
    base_distantion = 0.5

    def __init__(self, shop_address, despensary_id):
        self.geolocator = GeoLocator()
        self.__shop_address = self.geolocator.get_latitude_longtitude(shop_address)
        self.__hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"
        self.__dispensaryId = despensary_id

    def get_delivery_info(self, address):
        time.sleep(3)
        city, zipcode, state, lat, lng = self.geolocator.get_city_state_zipcode_lat_long(address)
        _city = '' or city
        zipcode = '' or zipcode
        url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{_city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%20{zipcode}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
        response = requests.get(url=url, headers=HEADERS)
        if response.status_code == 200:
            delivery_info = response.json()['data']['getAddressBasedDispensaryData']['deliveryInfo']
            delivery_area_id = delivery_info['deliveryAreaId']
            fee = float(delivery_info['fee']) / 100
            fee_varies = delivery_info['feeVaries']
            minimum = float(delivery_info['minimum']) / 100
            minimum_varies = float(delivery_info['minimumVaries']) / 100
            within_bounds = delivery_info['withinBounds']
            return delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds
        else:
            print(f"Error with status code {response.status_code}")

    def multi_scan_total_area(self, store, address):
        # gevent.sleep(15)
        """scan total area and sort according radius zones with fee cost"""
        s = time.time()
        store = str(store).replace(' ', '')
        address = str(address).replace(' ', '')
        radians = [(0, 90), (90, 180), (180, 270), (270, 360)]
        jobs = [gevent.spawn(self._scan_delivery_perimeter, i[0], i[1]) for i in radians]
        print('------------------GEVENT FINISHED-----------------------')
        gevent.joinall(jobs)
        global_data = []
        for job in jobs:
            global_data.append(job.value)
        final_data = clean_data_and_save(list_of_circle_sections=global_data, store=store,
                                         address=address)
        e = time.time()
        print(f'Done in {e - s} seconds')
        return final_data

    def _scan_delivery_perimeter(self, degree, until):
        """find borders of delivery figure on map."""
        file_name = f'{degree} - {until}'
        start_point = self.__shop_address
        distantion = self.base_distantion
        degree = degree
        queue = Queue()
        queue.put(start_point)
        delivery_area = {}
        while degree <= until:
            print("DEGREE IS", degree)
            point = queue.get()
            point = self.get_next_radial_point(start_point=point, distantion=distantion, bearing=degree)
            gevent.sleep(0.5)
            delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds = self.get_delivery_info(point)
            gevent.sleep(0.5)
            print(
                f"delivery_area_id - {delivery_area_id}, fee -{fee}, fee -{fee_varies}, min.varies -{minimum_varies}, minimum-{minimum}, within_bounds-{within_bounds}")
            if delivery_area_id is not None and within_bounds is True:
                if fee in delivery_area:
                    if degree in delivery_area[fee]:
                        if distantion in delivery_area[fee][degree]:
                            delivery_area[fee][degree][distantion].append(point)
                            delivery_area[fee][degree][distantion].append(f"min order - {minimum}")
                        else:
                            delivery_area[fee][degree][distantion] = [point, f"min order - {minimum}"]
                    else:
                        delivery_area[fee][degree] = {distantion: [point]}
                else:
                    delivery_area[fee] = {degree: {distantion: [point]}}
                print(f"delivery_area is--->")
                pprint.pprint(delivery_area)
                distantion += self.step
                queue.put(point)
            else:
                degree += 10
                print("Not delivery area")
                distantion = self.base_distantion
                print(f"changed degree to {degree} and distantion to {distantion}")
                point = start_point
                queue.put(point)
        return delivery_area

    def get_next_radial_point(self, start_point, distantion, bearing):
        bearing = float(bearing)
        end_point = distance(kilometers=distantion).destination(start_point, bearing)
        print(f"Coordinates of point at distance {distantion} km {bearing} degrees:"
              f" {end_point.latitude}, {end_point.longitude}")
        return end_point.latitude, end_point.longitude

    def get_neighbors(self, point, counter, direction='right'):
        """get nearest points on map at the selected direstion"""
        while True:
            neighbor = self.geolocator.step_from(point, direction=direction, multiplicator=counter)
            print(f"neighbor is {neighbor}")
            time.sleep(5)
            return neighbor
