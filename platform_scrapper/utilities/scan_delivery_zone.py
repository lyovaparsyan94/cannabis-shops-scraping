import json
import pprint
import time
import gevent
import requests
from data_collector import clean_data
from geo import GeoLocator
from gevent.queue import Queue
from geopy.distance import distance
from platform_scrapper.configs.constants import HEADERS


class ScanDutchieDelivery:
    half_km = GeoLocator.half_km
    step = 0.4
    # step = 2.8
    base_distantion = 1.5

    def __init__(self, shop_address, despensary_id, store, state, coordinates):
        self.geolocator = GeoLocator()
        # self.__shop_address = self.geolocator.get_latitude_longtitude(shop_address, store=store, state=state)
        self.__shop_address = coordinates[1], coordinates[0]
        self.__hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"
        self.__dispensaryId = despensary_id

    def get_delivery_info(self, address):
        gevent.sleep(5)
        city, zipcode, state, lat, lng = self.geolocator.get_city_state_zipcode_lat_long(address)
        _city = '' or city
        zipcode = '' or zipcode
        url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{_city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%20{zipcode}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
        response = requests.get(url=url, headers=HEADERS)
        if response.status_code == 200:
            delivery_info = response.json()['data']['getAddressBasedDispensaryData']['deliveryInfo']
            delivery_area_id = delivery_info['deliveryAreaId']
            fee = delivery_info.get('fee', None)
            if fee:
                fee = float(fee) / 100
            fee_varies = delivery_info['feeVaries']
            minimum = delivery_info.get('minimum', None)
            if minimum:
                minimum = float(minimum) / 100
            minimum_varies = delivery_info.get('minimumVaries', None)
            if minimum_varies:
                minimum_varies = float(minimum_varies) / 100
            within_bounds = delivery_info['withinBounds']
            print(f"within_bounds ----- {within_bounds}!!!!!!!!!!!!!!!!!!!!!!!!!")
            if within_bounds:
                if fee is False or fee is None:
                    fee = 0
                    print(f'within_bounds {within_bounds is True}, fee is False or None {fee in (False, None)} so fee = {fee}')
            return delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds
        else:
            print(f"Error with status code {response.status_code}")

    def multi_scan_total_area(self, store, address):
        """scan total area and sort according radius zones with fee cost"""
        store1 = str(store).replace(" ", '_').replace("'", '').capitalize()
        address1 = str(address).replace(" ", '_').replace("'", '').capitalize()
        filename = store1 + address1
        global_data = []
        try:
            s = time.time()
            radians = [(0, 72), (72, 144), (144, 216), (216, 288), (288, 360)]
            print(f'------------------GEVENT STARTED {store} {address}-----------------------')
            jobs = [gevent.spawn(self._scan_delivery_perimeter, i[0], i[1]) for i in radians]
            gevent.joinall(jobs)
            print(f'------------------GEVENT FINISHED {store} {address}-----------------------')
            for job in jobs:
                global_data.append(job.value)
            final_data = clean_data(list_of_circle_sections=global_data, store=store, address=address)
            with open(f"t_{filename}.json", "w") as j:
                json.dump(global_data, j)
            e = time.time()
            print(f'Done in {e - s} seconds')
            return final_data, f"{filename}"
        except Exception:
            print("Error in scanning")

    def _scan_delivery_perimeter(self, degree, until):
        """find borders of delivery figure on map."""
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
            delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds = [None] * 6
            try:
                get_delivery_info = self.get_delivery_info(point)
                if get_delivery_info:
                    delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds = get_delivery_info
            except TypeError as e:
                print("Error with getting delivery info:", e)
            print(
                f"delivery_area_id - {delivery_area_id}, fee -{fee}, fee - {fee_varies}, min.varies -{minimum_varies}, minimum-{minimum}, within_bounds-{within_bounds}")
            if within_bounds:
                print(f"within_bounds: {within_bounds}, fee-  {fee}")
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
                degree += 15
                distantion = self.base_distantion
                print(f"Not delivery area, changed degree to {degree} and distantion to {distantion}")
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
