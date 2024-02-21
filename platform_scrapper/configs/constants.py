DUTCHIE = 'Dutchie'
BUDDI = "Buddi"
LEAFLY = "Leafly"
WEEDMAPS = "Weedmaps"
TYMBER = 'Tymber'
TECHPOS = 'Techpos'
TENDY = 'Tendy'
BUDLER = 'Budler'
WAIO = 'WAIO'
Fire_and_Flower = 'Fire & Flower'

dutchie_markers = ["dutchie.com/api/", "dutchie--embed__styles", "dutchie-iframe", "dutchie--embed__iframe",
                   'href="https://tags.cnna.io/dutchie-iframe', "div.homepage-carousel-sections__Sections-sc-13b41re",
                   'images.dutchie.com', "dutchie--skip_to_menu_styles", "dutchie--back_to_top_styles",
                   "Dutchie Menu", 'dutchie--back-to-top', "dutchie--embed", "api.dutchie.com"]

buddi_markers = ["app.buddi.", "www.budside.com", "buddi-notification", "//app.buddi.io/css/ropis/tailwind",
                 "//app.buddi.io", ".buddi-online-menu",
                 'id="buddi-em-menu"', "buddi-app", "buddi-online-menu", "https://static.buddi.io/", "static.buddi.io/",
                 "buddi_field"
                 ]

weedmaps_markers = []

leafly_markers = []

tymber_markers = ["tymber.js", "surfside-tymber", "tymber-greenline", "TymberToast", "https://tymber", "TymberFooter",
                  "tymber", "https://tymber-s3"]
techpos_markers = ["https://techpos.ca", "E-commerce by TechPOS", "TechPOS"]

shop_markers = [
    "//a//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'order')]",
    "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'order')]",
    "//button//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shop')]",
    "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'daily')]",
]

weedmap_age = [
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
    "User-Agent": USER_AGENT,
    "Content-Type": "application/json",
}
ecommerse_providers = [DUTCHIE, BUDDI, LEAFLY, WEEDMAPS, TYMBER, TECHPOS, TENDY, BUDLER, WAIO, Fire_and_Flower]
ended_licension = "Public Notice Period: Ended"
