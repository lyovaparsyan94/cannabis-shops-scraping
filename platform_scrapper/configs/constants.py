DUTCHIE = 'Dutchie'
BUDDI = "Buddi"
LEAFLY = "Leafly"
WEEDMAPS = "Weedmaps"

dutchie_iframe = "dutchie--embed__iframe"
dutchie_plus_button = ""
dutchie_shop_selector = "div.homepage-carousel-sections__Sections-sc-13b41re"

dutchie_markers = ["dutchie.com/api/", "dutchie--embed__styles", "dutchie-iframe",
                   'href="https://tags.cnna.io/dutchie-iframe',
                   'images.dutchie.com', "dutchie--skip_to_menu_styles", "dutchie--back_to_top_styles",
                   "Dutchie Menu", 'dutchie--back-to-top', "dutchie--embed", "api.dutchie.com"]

weedmaps_markers = [

]
leafly_markers = [

]

buddi_markers = ["app.buddi.", "www.budside.com", "buddi-notification", "//app.buddi.io/css/ropis/tailwind",
                 "//app.buddi.io", ".buddi-online-menu",
                 'id="buddi-em-menu"', "buddi-app", "buddi-online-menu", "https://static.buddi.io/", "static.buddi.io/",
                 "buddi_field"
                 ]

shop_markers = [
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'order')]",
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'order')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'daily')]",
]

weedmap_no_bot = [
    "//p[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'press')]",
    "//p[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hold')]",
    "//p[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'Нажмите')]",
    "//p[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'удерживайте')]",
]

age_xpath_list = [
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]",
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old enough')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old enough')]",
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old')]",
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'OLD')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'enough')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'ENOUGH')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]",
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old enough')]",
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old enough')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'old')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'OLD')]",
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'enough')]",
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'ENOUGH')]",
]

age_select = [
    "//option[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/json",
}

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

consumer_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Cookie": "_ga_1QQ3EPGGJ3=GS1.1.1702054947.1.1.1702055577.60.0.0; _ga_4TSZ0LK22W=GS1.1.1702150075.2.0.1702150153.60.0.0; _ga_7F3HGF7PL4=GS1.1.1702480932.1.1.1702481847.60.0.0; _ga_5CCKH1MX6Y=GS1.1.1702649940.1.0.1702649960.40.0.0; _gid=GA1.2.1433509371.1702809491; __cflb=04dToaXWHAPESU8RyBQBc8Yta2dmM5dTc3JC5ZvpMD; _gat=1; _gat_UA-101536475-5=1; _ga=GA1.2.1605833789.1702809491; _ga_FZN7LD29Z4=GS1.1.1702813263.2.1.1702817191.0.0.0"
}