import pandas as pd

import numpy as np
import json
import geog
import shapely.geometry
import geopandas as gpd
import folium
from shapely import wkt, geometry
import json
from pprint import pprint
from folium import plugins
from openrouteservice import client, places

data = pd.read_csv('data_with_counts_8351.csv', index_col = 'id')
cta_json = gpd.read_file('cta_entrances.geojson')
api_key='5b3ce3597851110001cf6248f4a7fee5db334593bc67406f86071778'
clnt = client.Client(key=api_key)

def shapes(long,lat, d = 1000):
    p = shapely.geometry.Point([long,lat])
    n_points = 100
    #d = 1000  # meters
    angles = np.linspace(0, 360, n_points)
    polygon = geog.propagate(p, angles, d)
    wkt_str = shapely.geometry.Polygon(polygon).wkt
    aoi_geom = wkt.loads(wkt_str)
    poly = shapely.geometry.Polygon(polygon)
    aoi_coords = list(aoi_geom.exterior.coords) # get coords from exterior ring
    aoi_coords = [(y,x) for x,y in aoi_coords] # swap (x,y) to (y,x). Really leaflet?!
    aoi_centroid = aoi_geom.centroid # Kreuzberg center for map center
    return poly 

for listing in range(len(data)):
    base_long = data.longitude.iloc[listing]
    base_lat = data.latitude.iloc[listing]
    routes = {}
    walk_time = []
    list_loc = [[base_long,base_lat]]
    n = 0 
    for name, point, line, x in zip(cta_json['name'], cta_json['geometry'], cta_json['line'], range(len(cta_json))):
        times = []
        if point.within(shapes(base_long,base_lat)):
            cta_loc = [[point.x,point.y]] 
            route_coords =  list_loc + cta_loc  
            request = {'coordinates': route_coords,
            'profile': 'foot-walking',
            'geometry': 'true',
            'format_out': 'geojson'}
            route = clnt.directions(**request)
            #routes[n] = route
            times.append(route['features'][0]['properties']['summary']['duration'])
            #n += 1
        else: 
            point.within(shapes(base_long,base_lat,d=5000))
            cta_loc = [[point.x,point.y]] 
            route_coords =  list_loc + cta_loc  
            request = {'coordinates': route_coords,
            'profile': 'foot-walking',
            'geometry': 'true',
            'format_out': 'geojson'}
            route = clnt.directions(**request)
            #routes[n] = route
            times.append(route['features'][0]['properties']['summary']['duration'])
            #n += 1
        walk_time.append(min(times))
        
        
