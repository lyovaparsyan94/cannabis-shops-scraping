import requests
# get_city_state_zipcode_lat_long
dispensaryId = "5eb9a5221c1db800f8bd2a7d"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/json",
}
url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables=%7B%22dispensaryFilter%22%3A%7B%22cNameOrID%22%5eb9a5221c1db800f8bd2a7d%22%2C%22city%22%3A%22Burlington%22%2C%22nearLat%22%3A43.32485459999999%2C%22nearLng%22%3A-79.79568019999999%2C%22destinationTaxState%22%3A%22ON%22%2C%22destinationTaxZipcode%22%3A%22L7R%201A1%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22%7D%7D"
# url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={%22dispensaryFilter%22:{%22cNameOrID%22:%225f7d38d029883400facd32a9%22,%22city%22:%22Burlington%22,%22nearLat%22:43.32485459999999,%22nearLng%22:-79.79568019999999,%22destinationTaxState%22:%22ON%22,%22destinationTaxZipcode%22:%22L7R%201A1%22}}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22}}"
# url = "https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables{%22dispensaryFilter%22:{%22cNameOrID%22:%225f7d38d029883400facd32a9%22,%22city%22:%%22,%22nearLat%22:43.32485459999999,%22nearLng%22:-79.79568019999999,%22destinationTaxState%22:%22ON%22,%22destinationTaxZipcode%22:%22L7R%201A1%22}}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%224f415a7b945a5c58d2cf92ace12a3e24e40815f05f0755adc285d86f584d15c3%22}}"
r = requests.get(url, headers=HEADERS)
print(r.json())
