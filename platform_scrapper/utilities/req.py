import requests
import pprint

# dispensaryId = "tweed-ajax"
dispensaryId = "tokyo-smoke-hanover-10th"
city = "Whitby"
state = "ON"
zipcode = "L1N"
lat = 43.8599
lng = -78.936
hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"
url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
# url = "https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22blue-bird-cannabis%22%2C%22city%22%3A%22Kanata%22%2C%22state%22%3A%22ON%22%2C%22zipcode%22%3A%22K2T%201J8%22%2C%22lat%22%3A45.311257%2C%22lng%22%3A-75.917461%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b%22%7D%7D"
# url = "https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22tweed-ajax%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b%22%7D%7D"
# url = "https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22tokyo-smoke-hanover-10th%22%2C%22city%22%3A%22Pickering%22%2C%22state%22%3A%22ON%22%2C%22zipcode%22%3A%22L1V%201B5%22%2C%22lat%22%3A43.8301685%2C%22lng%22%3A-79.0966997%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b%22%7D%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Cookie": "_ga_1QQ3EPGGJ3=GS1.1.1702054947.1.1.1702055577.60.0.0; _ga_4TSZ0LK22W=GS1.1.1702150075.2.0.1702150153.60.0.0; _ga_7F3HGF7PL4=GS1.1.1702480932.1.1.1702481847.60.0.0; _ga_5CCKH1MX6Y=GS1.1.1702649940.1.0.1702649960.40.0.0; _gid=GA1.2.1433509371.1702809491; __cflb=04dToaXWHAPESU8RyBQBc8Yta2dmM5dTc3JC5ZvpMD; _gat=1; _gat_UA-101536475-5=1; _ga=GA1.2.1605833789.1702809491; _ga_FZN7LD29Z4=GS1.1.1702813263.2.1.1702817191.0.0.0"
}

# res = requests.get(url=url, headers=headers)
# pprint.pprint(res.status_code)
# pprint.pprint(res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo'])


print('' or False)
print('asdasd' or None)








