import pprint
import requests

# dispensaryId = "5eb9a5221c1db800f8bd2a7d"
# # city = "Whitby"
# city = "Toronto"
# state = "ON"
# zipcode = ""
# lat = ''
# lng = ''
hsh = "2213461f73abf7268770dfd05fe7e10c523084b2bb916a929c08efe3d87531977b"
src_id = '6548f8995592fc0009fbe149'

consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID' \
               '":"%s"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815' \
               'f05f0755adc285d86f584d15c3"}}' % src_id
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Cookie": "_ga_1QQ3EPGGJ3=GS1.1.1702054947.1.1.1702055577.60.0.0; _ga_4TSZ0LK22W=GS1.1.1702150075.2.0.1702150153.60.0.0; _ga_7F3HGF7PL4=GS1.1.1702480932.1.1.1702481847.60.0.0; _ga_5CCKH1MX6Y=GS1.1.1702649940.1.0.1702649960.40.0.0; _gid=GA1.2.1433509371.1702809491; __cflb=04dToaXWHAPESU8RyBQBc8Yta2dmM5dTc3JC5ZvpMD; _gat=1; _gat_UA-101536475-5=1; _ga=GA1.2.1605833789.1702809491; _ga_FZN7LD29Z4=GS1.1.1702813263.2.1.1702817191.0.0.0"
}

res = requests.get(url=consumer_url, headers=headers)
# pprint.pprint(res.json()['data']['filteredDispensaries'][0]['location'])
# resp = res.json()['data']['getAddressBasedDispensaryData']['deliveryInfo']['deliveryAreaId']
resp = res.json()['data']['filteredDispensaries']
address = res.json()['data']['filteredDispensaries'][0]['address']
delivery_hours = res.json()['data']['filteredDispensaries'][0]['deliveryHours']['Monday']['active']
delivery_enabled = res.json()['data']['filteredDispensaries'][0]['orderTypesConfig']['delivery']['enabled']
url_with_endpoint = res.json()['data']['filteredDispensaries'][0]['embeddedMenuUrl']
cName = res.json()['data']['filteredDispensaries'][0]['cName']
city = res.json()['data']['filteredDispensaries'][0]['location']['city']
coordinates = res.json()['data']['filteredDispensaries'][0]['location']['geometry']['coordinates']
ln1 = res.json()['data']['filteredDispensaries'][0]['location']['ln1']
ln2 = res.json()['data']['filteredDispensaries'][0]['location']['ln2']
state_short = res.json()['data']['filteredDispensaries'][0]['location']['state']
zipcode = res.json()['data']['filteredDispensaries'][0]['location']['zipcode']
# url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{dispensaryId}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{lat}%2C%22lng%22%3A{lng}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
url = f"https://dutchie.com/graphql?operationName=GetAddressBasedDispensaryData&variables=%7B%22input%22%3A%7B%22dispensaryId%22%3A%22{cName}%22%2C%22city%22%3A%22{city}%22%2C%22state%22%3A%22{state_short}%22%2C%22zipcode%22%3A%22%201B9%22%2C%22lat%22%3A{coordinates[0]}%2C%22lng%22%3A{coordinates[1]}%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%{hsh}%22%7D%7D"
res = requests.get(url=consumer_url, headers=headers)
# pprint.pprint(delivery_enabled)
print(len("-------------------------------------------------------------"))