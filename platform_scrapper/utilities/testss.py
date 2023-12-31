import requests

# name = 'Burlington Cannabis'.replace(' ', '-').lower()
# print(name)
# # url = 'https://api.dutchie.com/api/v2/embedded-menu/60ef6512cfdcd400d5411d76.js'
# url = 'https://www.burlingtoncannabisco.ca/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Content-Type': 'application/json'}
#
# response = requests.get(url, headers=headers)
# print(response.text)
import urllib.parse

city = "Paris"
country = "France"
url = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + city + "+" + country +"&format=json&limit=1"

response = requests.get(url).json()
print(response[0]["lat"])
print(response[0]["lon"])