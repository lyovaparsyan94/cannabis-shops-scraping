import json
import pprint
import time
import gevent
import requests
from utilities.file_handler import file_name_maker
from platform_scrapper.src.geo import GeoLocator
from gevent.queue import Queue
from geopy.distance import distance
from utilities.file_modifier import clean_data
from platform_scrapper.configs.constants import BUDDI, DUTCHIE, HEADERS
from platform_scrapper.configs.file_constantns import CONFIG_FILE_PATH, COLLECT_DIR
from utilities.file_handler import load_config


class ScanDutchieDelivery:
    step = 0.4
    base_distantion = 0.0

    def __init__(self, shop_address, despensary_id, store, provider, state, coordinates, buddi_params=None):
        self.geolocator = GeoLocator()
        self.request_counter = 0
        self.degree = 15
        self.state = state
        self.__shop_address = self._get_shop_address(store=store, shop_address=shop_address, state=self.state)
        self.__hsh = load_config(CONFIG_FILE_PATH)['DUTCHIE']['request_key']
        self.__dispensaryId = despensary_id
        self.buddi_params = buddi_params

    def _get_shop_address(self, coordinates=None, store=None, shop_address=None, state=None):
        if coordinates:
            return coordinates[1], coordinates[0]
        else:
            return self.geolocator.get_latitude_longtitude(shop_address, store=store, state=state)

    def get_delivery_info(self, address):
        # gevent.sleep(1.2)
        # working alternative variant
        # _city, zipcode, stat, lat, lng = self.geolocator.get_city_state_zipcode_lat_long(address)

        _city = ''
        zipcode = ''
        lat = address[0]
        lng = address[1]
        url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{_city}%22%2C%22state%22%3A%22{self.state}%22%2C%22zipcode%22%3A%22%20{zipcode}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
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
            print(f"within_bounds ----- {within_bounds}!")
            if within_bounds:
                if fee is False or fee is None:
                    fee = 0
                    print(
                        f'within_bounds {within_bounds is True}, fee is False or None {fee in (False, None)} so fee = {fee}')
            return delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds
        else:
            print(f"Error with status code {response.status_code}")

    def multi_scan_total_area(self, store, address, provider=DUTCHIE, buddi_params=None):
        """scan total area and sort according radius zones with fee cost"""
        filename = file_name_maker(store, address)
        global_data = []
        radians = [(0, 72), (72, 144), (144, 216), (216, 288), (288, 360)]
        s = time.time()
        try:
            print(f'------------------GEVENT STARTED {store} {address}-----------------------')
            if provider == DUTCHIE:
                jobs = [gevent.spawn(self._scan_dutchie_delivery_perimeter, i[0], i[1]) for i in radians]
            elif provider == BUDDI:
                jobs = [gevent.spawn(self._scan_buddi_delivery_perimeter, degree=i[0], until=i[1]) for i
                        in
                        radians]
            gevent.joinall(jobs)
            for job in jobs:
                global_data.append(job.value)
            print(f'------------------GEVENT FINISHED {store} {address}-----------------------')
            final_data = clean_data(list_of_circle_sections=global_data, store=store, address=address)
            with open(fr"{COLLECT_DIR}\t_{filename}.json", "w") as j:
                json.dump(global_data, j)
            return final_data, f"{filename}"
        except Exception:
            print("Error in scanning")
        finally:
            e = time.time()
            print(f"Collected delivery info in {e - s} seconds, provider: {provider}")

    def _scan_dutchie_delivery_perimeter(self, degree, until, state=''):
        """find borders of delivery figure on map on Dutchie based ecommerce provider's shops"""
        start_point = self.__shop_address
        distantion = self.base_distantion
        degree = degree
        queue = Queue()
        queue.put(start_point)
        delivery_area = {}
        while degree <= until:
            print(f"DEGREE IS {degree} / {until}")
            point = queue.get()
            distantion_checker = distantion
            point = self.get_next_radial_point(start_point=point, distantion=distantion, bearing=degree)
            delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds = [None] * 6
            try:
                get_delivery_info = self.get_delivery_info(point)
                print(f'Count of requests: {self.request_counter}')
                self.request_counter += 1
                if get_delivery_info[-1]:
                    delivery_area_id, fee, fee_varies, minimum_varies, minimum, within_bounds = get_delivery_info
            except TypeError as e:
                print("Error with getting delivery info:", e)
            print(
                f"delivery_area_id - {delivery_area_id}, fee -{fee}, fee_varies - {fee_varies}, min.varies -{minimum_varies}, minimum-{minimum}, within_bounds-{within_bounds}")
            if within_bounds:
                print(f"within_bounds: {within_bounds}, fee-  {fee}")
                self.collect_delivery_info(fee=fee, delivery_area=delivery_area, minimum=minimum, degree=degree,
                                           distantion=distantion, point=point)
                print(f"step: {self.step}, distance: {distantion_checker}, degree: {self.degree}")
                if distantion_checker > 10:
                    self.step = 1
                    self.degree = 20
                elif distantion_checker > 15:
                    self.step = 1.5
                    self.degree = 22
                elif distantion_checker > 20:
                    self.step = 2
                    self.degree = 24
                elif distantion_checker > 25:
                    self.step = 2.5
                    self.degree = 28
                elif distantion_checker > 30:
                    self.step = 3
                    self.degree = 32
                pprint.pprint(delivery_area)
                distantion += self.step
                queue.put(point)
            else:
                distantion = self.base_distantion
                degree += self.degree
                print(f"Not delivery area, changed degree to {degree} and distantion to {distantion}")
                point = start_point
                queue.put(point)
        print(f'made {self.request_counter} requests for this shop')
        return delivery_area

    @staticmethod
    def get_next_radial_point(start_point, distantion, bearing):
        """get point on map with X distantion and Y degree"""
        bearing = float(bearing)
        print("trying get next point ...")
        gevent.sleep(2)
        end_point = distance(kilometers=distantion).destination(start_point, bearing)
        print(f"next point at distance {distantion} km and {bearing} degrees:"
              f" {end_point.latitude}, {end_point.longitude}")
        return end_point.latitude, end_point.longitude

    def get_neighbors(self, point, counter, direction='right'):
        """get nearest points on map at the selected direstion"""
        while True:
            neighbor = self.geolocator.step_from(point, direction=direction, multiplicator=counter)
            print(f"neighbor is {neighbor}")
            time.sleep(5)
            return neighbor

    def _scan_buddi_delivery_perimeter(self, degree: int = 0, until: int = 0, radius: int = 0, fee: int = -1,
                                       minimum: int = -1):
        """find borders of delivery figure on map of Buddi based ecommerce provider's shops"""
        if self.buddi_params:
            radius = self.buddi_params['radius']
            fee = self.buddi_params['fee']
            minimum = self.buddi_params['minimum']
        start_point = self.__shop_address
        distantion = radius
        queue = Queue()
        queue.put(start_point)
        delivery_area = {}
        while degree <= until:
            print(f"DEGREE IS {degree} / {until}")
            point = queue.get()
            point = self.get_next_radial_point(start_point=point, bearing=degree, distantion=distantion)
            print(f'Count of made requests: {self.request_counter}')
            self.request_counter += 1
            if distantion <= radius:
                self.collect_delivery_info(fee=fee, delivery_area=delivery_area, minimum=minimum, degree=degree,
                                           distantion=distantion, point=point)
                distantion += radius
                queue.put(point)
            else:
                distantion = self.base_distantion
                degree += self.degree
                print(f"Changed degree to {degree} and distantion to {distantion}")
                point = start_point
                queue.put(point)
        print(f'made {self.request_counter} requests for this Buddi shop')
        pprint.pprint(delivery_area)
        return delivery_area

    @staticmethod
    def collect_delivery_info(fee, delivery_area, minimum, degree, distantion, point):
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
        pprint.pprint(delivery_area)
