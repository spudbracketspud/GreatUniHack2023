import json
import time
import urllib.error
import urllib.parse
import urllib.request
import ssl
import math

API_KEY = "AIzaSyBhCM71caTVu_CY8UWTR6NjBzmcc3poOR0"
VIEWPORT_BASE_URL = "https://tile.googleapis.com/tile/v1/viewport"
TILES_BASE_URL = "https://tile.googleapis.com/v1/2dtiles"  
SESSION_BASE_URL = "https://tile.googleapis.com/v1/createSession"
SSL_CONTEXT = ssl._create_unverified_context() #DO NOT PUSH TO PRODUCTION

"""
Generic function for posting url requests

url: base url for post request/full url for a get request
data: for post request, data required as encoded request. do not provide for get requests
json_key: key for required data within json response (if needed).
"""
def make_request(url,data=None,json_key=None):
    current_delay = 0.1 # set initial retry delay to 100ms
    max_delay = 3 # set max retry delay to 5s

    while True:
        try:
            # get API response
            if data is None:
                #get request
                response = urllib.request.urlopen(url,context=SSL_CONTEXT)
            else:
                #post request
                response = urllib.request.urlopen(url,data,context=SSL_CONTEXT)

        except urllib.error.URLError as error:
            print(error)
            pass
        else:
            # if no IOError, parse result
            if response.status == 200:
                # if no errors, return the list of tiles
                if json_key == None:
                    return
                result = json.load(response)
                return result[json_key]

        if current_delay > max_delay:
            raise Exception("Too many retry attempts")

        print("Waiting", current_delay, "seconds before retrying.")

        time.sleep(current_delay)
        current_delay *= 2  # increase the delay each time we retry

"""
Fetches a token for making requests, estabishes for the tile types

map_type: tile type (roadmap, satellite, terrain, streetview)
styles: optional dictionary of style information, see https://developers.google.com/maps/documentation/tile/style-reference
zoom: Max zoom level of the tiles
"""
def fetch_session_token(API_KEY,map_type,styles=None):

    #join url parts together
    params = urllib.parse.urlencode(
        {
        "key":API_KEY,
        "mapType":map_type,
        "language":"en-UK",
        "region":"UK",
        "imageFormat":"png"
        }
    ).encode()

    if styles is not None:
        params["styles"] = styles

    return make_request(SESSION_BASE_URL,params,json_key="session")



"""
Fetches the list of tile co-ordinates within a specified
rectangular section of the world map.

lat_bound: Pair of integers in the range (-90,90) defining the north/south bounds of the rectangle.
lat_bound: Pair of integers in the range (-90,90) defining the east/west bounds of the rectangle.
zoom: Max zoom level of the tiles
"""
def fetch_map_tile_coords(API_KEY,SESSION_TOKEN,lat_bound,long_bound,zoom):

    # join url parts together in one string
    params = urllib.parse.urlencode(
        {
        "session":SESSION_TOKEN,"key":API_KEY,
        "zoom":zoom,
        "north":lat_bound[0],"south":lat_bound[1],
        "east":long_bound[0],"west":long_bound[1]
        }
    )

    url = f"{VIEWPORT_BASE_URL}?{params}"

    return make_request(url,json_key="maxZoomRects")

def fetch_map_tile_images(API_KEY,SESSION_TOKEN,lat,lon,zoom):

    lat_rad = (lat*math.pi) / 180
    if lat_rad == 0:
        lat_rad += 0.0001
    
    n = 2 ** zoom
    tile_x = int(n * ((lon + 180) / 360))
    tile_y = int(n * (1 - (math.log(math.tan(lat_rad) + (1/math.sin(lat_rad))) / math.pi)) / 2)
    print([tile_x,tile_y])
  
    params = urllib.parse.urlencode(
        {
        "session":SESSION_TOKEN,"key":API_KEY,
        "orientation":0
        }
    )

    url = f"{TILES_BASE_URL}/{zoom}/{tile_x}/{tile_y}?{params}"
    print(url)

    make_request(url)



SESSION_TOKEN = fetch_session_token(API_KEY,"roadmap")
lat,lon = 60,22
map_tile_coords = fetch_map_tile_coords(API_KEY,SESSION_TOKEN,(60,65),(20,22),22)
zoom = map_tile_coords[-1]["maxZoom"]
print(fetch_map_tile_images(API_KEY,SESSION_TOKEN,lat,lon,zoom))
