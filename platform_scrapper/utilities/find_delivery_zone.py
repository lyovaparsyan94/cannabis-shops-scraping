# import time
# import requests
# from queue import Queue
# from platform_scrapper.configs.constants import NO_DELIVERY_AREA, HEADERS
#
from pprint import pprint
#
# def is_delivery(self, address):
#     time.sleep(5)
#     city, zipcode, state, lat, lng = self.geolocator.get_city_state_zipcode_lat_long(address)
#     _city = '' or city
#     zipcode = '' or zipcode
#     url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{_city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%20{zipcode}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
#     # url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
#     # url = "https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22tweed-ajax%22%2C%22city%22%3A%22Ajax%22%2C%22state%22%3A%22L1S%201P2%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A43.84666045%2C%22lng%22%3A-79.0165227505899%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b%22%7D%7D"
#     consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"%s"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}' % (
#         self.__dispensaryId)
#     # consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"tweed-ajax"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}'
#     res = requests.get(url=url, headers=HEADERS)
#     status = res.status_code
#     response = res.json()
#     if status == 200:
#         # 9483 Mississauga Rd, Brampton, ON L6X 0Z8, Canada
#         # 3140 Argentia Rd Unit 1, Mississauga, ON L5N 0B1, Canada
#         delivery_info = response['data']['getAddressBasedDispensaryData']['deliveryInfo']
#         withbounds = delivery_info['withinBounds']
#         x = delivery_info['deliveryAreaId']
#         print(delivery_info['deliveryAreaId'])
#         if x == "Out of Region":
#             return NO_DELIVERY_AREA, delivery_info
#         if delivery_info['deliveryAreaId'] is None:
#             return None, delivery_info
#         if withbounds:
#             return True, delivery_info
#         else:
#             print(status)
#             print(f"Withbounds {withbounds}")
#             print(delivery_info)
#             return False, delivery_info
#     else:
#         c_resp = requests.get(url=consumer_url, headers=HEADERS)
#         if c_resp.status_code == 200:
#             c_resp_json = c_resp.json()
#             c_delivery_info = c_resp_json['data']['filteredDispensaries'][0]['enabledOrderTypes']
#             if c_delivery_info:
#                 if c_delivery_info['delivery']:
#                     return c_delivery_info['delivery'], c_delivery_info
#             else:
#                 print("Delivery area status", c_resp.status_code)
#                 return None, c_delivery_info
#
#
# def find_delivery_perimeter(self):
#     """find  borders of delivery figure on map."""
#     start_point = self.__shop_address
#     distantion = 4
#     degree = 90
#     queue = Queue()
#     queue.put(start_point)
#     perimeter = []
#     previous_fee = None
#     current_fee = None
#     delivery_area_fee_min_order = {}
#     previous_point = None
#     current_point = None
#     while not queue.empty() and degree <= 360:
#         point = queue.get()
#         new_point = self.get_bearing_direction_point(start_point=point, distantion=distantion, bearing=degree)
#         delivery_status, delivery_info = self.check_delivery(new_point)
#         fee = delivery_info['fee']
#         minimum_order = delivery_info['minimum']
#         if delivery_status == NO_DELIVERY_AREA:
#             print(NO_DELIVERY_AREA)
#             perimeter.append(new_point)
#             degree += 15
#             if delivery_area_fee_min_order.get(fee, None) is None:
#                 delivery_area_fee_min_order[fee] = {'perimeter': [], 'minimum_order': minimum_order}
#             else:
#                 delivery_area_fee_min_order[fee]['perimeter'] += perimeter
#                 delivery_area_fee_min_order[fee]['minimum_order'] += minimum_order
#             queue.put(current_point)
#         elif delivery_status is None:
#             previous_point = current_point
#             current_point = new_point
#             next_point = self.get_bearing_direction_point(start_point=current_point, distantion=distantion + 1,
#                                                           bearing=degree)
#             next_point_status, next_point_info = self.check_delivery(next_point)
#             if next_point_status is None:
#                 perimeter.append(current_point)
#                 degree += 15
#                 queue.put(current_point)
#                 if delivery_area_fee_min_order.get(fee, None) is None:
#                     delivery_area_fee_min_order[fee] = {'perimeter': [], 'minimum_order': minimum_order}
#                 else:
#                     delivery_area_fee_min_order[fee]['perimeter'] += perimeter
#                     delivery_area_fee_min_order[fee]['minimum_order'] += minimum_order
#             else:
#                 print("None--None")
#                 distantion += 1
#                 queue.put(current_point)
#                 continue
#         elif delivery_status:
#             # previous_point = current_point
#             # current_point = new_point
#             previous_fee = current_fee
#             current_fee = fee
#             distantion += 1
#             queue.put(new_point)
#         else:
#             perimeter.append(current_point)
#             degree += 15
#             print(f"changed degree to {degree}")
#             distantion = 1
#             previous_point, current_point = None, None
#             new_point = start_point
#             queue.put(new_point)
#             if delivery_area_fee_min_order.get(fee, None) is None:
#                 delivery_area_fee_min_order[fee] = {'perimeter': [], 'minimum_order': minimum_order}
#             else:
#                 delivery_area_fee_min_order[fee]['perimeter'] += perimeter
#                 delivery_area_fee_min_order[fee]['minimum_order'] += minimum_order
#         print(perimeter)
#         print(delivery_area_fee_min_order)
#     return perimeter
#
#
#     # def find_delivery_perimeter(self, direction="right"):
#     #     # Функция, которая находит края фигуры на карте.
#     #     # start_point - начальная точка на карте
#     #     start_point = self.__shop_address
#     #     counter = 1
#     #     queue = Queue()
#     #     queue.put(start_point)
#     #     perimeter = {
#     #         "left": {"distance": 0, "border point": 0, },
#     #         "right": {"distance": 0, "border point": 0},
#     #         "up": {"distance": 0, "border point": 0},
#     #         "down": {"distance": 0, "border point": 0},
#     #     }
#     #     # while not queue.empty():
#     #     #     print(counter)
#     #     #     point = queue.get()
#     #     #     perimeter[direction]["border point"] = point
#     #     #     neighbor_point = self.get_neighbors(point, counter, direction)
#     #     #     if self.check_delivery(neighbor_point):
#     #     #         distance = self.geolocator.measure_distantion(point, neighbor_point)
#     #     #         print("distance is", distance)
#     #     #         perimeter[direction]["border point"] = neighbor_point
#     #     #         perimeter[direction]["distance"] = int(distance)
#     #     #         queue.put(neighbor_point)
#     #     #         counter += 1
#     #     # print(perimeter)
#     #     # return perimeter
#     #     while not queue.empty():
#     #         print(counter)
#     #         point = queue.get()
#     #         perimeter[direction]["border point"] = point
#     #         neighbor_point = self.get_neighbors(point, counter, direction)
#     #         if self.check_delivery(neighbor_point):
#     #             distance = self.geolocator.measure_distantion(point, neighbor_point)
#     #             print("distance is", distance)
#     #             perimeter[direction]["border point"] = neighbor_point
#     #             perimeter[direction]["distance"] = int(distance)
#     #             queue.put(neighbor_point)
#     #             counter += 1
#     #     print(perimeter)
#     #     return perimeter
#
# def is_delivery(self, address):
#     time.sleep(5)
#     city, zipcode, state, lat, lng = self.geolocator.get_city_state_zipcode_lat_long(address)
#     _city = '' or city
#     zipcode = '' or zipcode
#     url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{_city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%20{zipcode}%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
#     # url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{self.__dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{self.__hsh}%22%7D%7D"
#     # url = "https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22tweed-ajax%22%2C%22city%22%3A%22Ajax%22%2C%22state%22%3A%22L1S%201P2%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A43.84666045%2C%22lng%22%3A-79.0165227505899%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b%22%7D%7D"
#     consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"%s"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}' % (
#         self.__dispensaryId)
#     # consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID":"tweed-ajax"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3"}}'
#     res = requests.get(url=url, headers=HEADERS)
#     status = res.status_code
#     response = res.json()
#     if status == 200:
#         # 9483 Mississauga Rd, Brampton, ON L6X 0Z8, Canada
#         # 3140 Argentia Rd Unit 1, Mississauga, ON L5N 0B1, Canada
#         delivery_info = response['data']['getAddressBasedDispensaryData']['deliveryInfo']
#         withbounds = delivery_info['withinBounds']
#         x = delivery_info['deliveryAreaId']
#         print(delivery_info['deliveryAreaId'])
#         if x == "Out of Region":
#             return NO_DELIVERY_AREA, delivery_info
#         if delivery_info['deliveryAreaId'] is None:
#             return None, delivery_info
#         if withbounds:
#             return True, delivery_info
#         else:
#             print(status)
#             print(f"Withbounds {withbounds}")
#             print(delivery_info)
#             return False, delivery_info
#     else:
#         c_resp = requests.get(url=consumer_url, headers=HEADERS)
#         if c_resp.status_code == 200:
#             c_resp_json = c_resp.json()
#             c_delivery_info = c_resp_json['data']['filteredDispensaries'][0]['enabledOrderTypes']
#             if c_delivery_info:
#                 if c_delivery_info['delivery']:
#                     return c_delivery_info['delivery'], c_delivery_info
#             else:
#                 print("Delivery area status", c_resp.status_code)
#                 return None, c_delivery_info
