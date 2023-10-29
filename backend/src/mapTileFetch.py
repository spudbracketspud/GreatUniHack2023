import json
import time
import urllib.error
import urllib.parse
import urllib.request
import ssl
import math

API_KEY = input()
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
                # if no errors, return the response json
                if json_key == None:
                    return
                result = json.load(response)
                return result[json_key]

        if current_delay > max_delay:
            raise Exception("Too many retry attempts")

        print("Waiting", current_delay, "seconds before retrying.")

        time.sleep(current_delay)
        current_delay *= 2  # increase the delay each time we retry


def fetch_image(url,path,filename):
    print(url)
    path = f"{path}/{filename}"
    current_delay = 0.1 # set initial retry delay to 100ms
    max_delay = 3 # set max retry delay to 5s

    while True:
        try:
            response = urllib.request.urlopen(url,context=SSL_CONTEXT)
        except urllib.error.URLError as error:
            print(error)
            pass
        else:
            if response.status == 200:
                img = response.read()
                with open(path,"wb") as handler:
                    handler.write(img)
                return

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
        "imageFormat":"png",
        "highDpi":"true"
        }
    ).encode()

    if styles is not None:
        params["styles"] = styles

    return make_request(SESSION_BASE_URL,params,json_key="session")



"""
Fetches a set of bounded rectangles in latitude and longitude with the maximum
zoom that can be obtained on that area, in descending order of size

lat_bound: Pair of integers in the range (-90,90) defining the north/south bounds of the rectangle.
lat_bound: Pair of integers in the range (-90,90) defining the east/west bounds of the rectangle.
zoom: Max zoom level of the tiles
"""
def fetch_map_tile_bounds(API_KEY,SESSION_TOKEN,lat_bound,lon_bound,zoom):

    # join url parts together in one string
    params = urllib.parse.urlencode(
        {
        "session":SESSION_TOKEN,"key":API_KEY,
        "zoom":zoom,
        "north":lat_bound[0],"south":lat_bound[1],
        "east":lon_bound[0],"west":lon_bound[1]
        }
    )

    url = f"{VIEWPORT_BASE_URL}?{params}"

    return make_request(url,json_key="maxZoomRects")

def fetch_map_tile_images(API_KEY,SESSION_TOKEN,lat_bound,lon_bound,zoom):
    tile_x0, tile_y0 = lat_lon_to_tile(lat_bound[0],lon_bound[0],zoom)
    tile_x1, tile_y1 = lat_lon_to_tile(lat_bound[1],lon_bound[1],zoom)

    for i in range(tile_y0,tile_y1+1):
        for j in range(tile_y0,tile_y1+1):


            params = urllib.parse.urlencode(
                {
                "session":SESSION_TOKEN,"key":API_KEY,
                }
            )

            url = f"{TILES_BASE_URL}/{zoom}/{i}/{j}?{params}"
            name = f"test{i}{j}"
            fetch_image(url,"captures",name)
"""
given a bounded rectangle by latitude and longitude
and the max zoom on that area
determine the zoom such that the resulting map tile would cover the whole area
"""
def zoom_out(lat_bound,lon_bound,zoom):
    tile_x0, tile_y0 = lat_lon_to_tile(lat_bound[0],lon_bound[0],zoom)
    tile_x1, tile_y1 = lat_lon_to_tile(lat_bound[1],lon_bound[1],zoom)

    print([tile_x0,tile_y0])
    print([tile_x1,tile_y1])

    tile_xgap = abs(tile_x1 - tile_x0) + 1
    tile_ygap = abs(tile_y1 -tile_y0) + 1

    print([tile_xgap,tile_ygap])

    zoom_diff = math.log(max(tile_xgap,tile_ygap),2)
    return math.floor(zoom - zoom_diff)


def lat_lon_to_tile(lat,lon,zoom):
    lat_rad = (lat*math.pi) / 180
    if math.sin(lat_rad) == 0:
        lat_rad += 0.0001

    n = 2 **(zoom)
    tile_x = math.floor(n * ((lon + 180) / 360))
    tile_y = math.floor(n * (1 - (math.log(math.tan(lat_rad) + (1/math.sin(lat_rad))) / math.pi)) / 2)

    return tile_x,tile_y

SESSION_TOKEN = fetch_session_token(API_KEY,"satellite")
lat = (40,40.5)
lon = (20,20.5)

"""obtain maximum zoom possible on latitude-longitude area
want the last item in the list as that gives the smallest area"""
map_tile_coords = fetch_map_tile_bounds(API_KEY,SESSION_TOKEN,lat,lon,10)
print(map_tile_coords)
max_zoom = map_tile_coords[-1]["maxZoom"]
fetch_map_tile_images(API_KEY,SESSION_TOKEN,lat,lon,max_zoom)

#determine whether this needs to be zoomed out to cover the whole area
# ideal_zoom = zoom_out(lat,lon,max_zoom)
# print([max_zoom,ideal_zoom])
# zoom = min(max_zoom,ideal_zoom)

