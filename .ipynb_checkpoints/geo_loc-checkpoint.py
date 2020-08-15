import pandas as pd
### packages for geo data 
import requests
import osmnx as ox
import re
import openrouteservice as ors

### picking the csv file 
def choose_csv():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    data = pd.read_csv(filename,index_col=['id'])
    return data

def pois_amenities(data):
    tags = {'amenity':['restaurant', 'bar', 'cafe','university']}
    restaurants = []
    bars = []
    cafes = []
    unis = []
    data_temp = data
    for x in range(len(data_temp)):
        pois_temp = ox.pois_from_point(point=(data_temp.latitude.iloc[x],data_temp.longitude.iloc[x]), dist=1000, tags=tags)  
        if 'amenity' in pois_temp:
            restaurants.append(len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')))  # if len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')) > 0 else restaurants.append(0) 
            bars.append(len(pois_temp[pois_temp['amenity']=='bar'].dropna(axis=1, how='any')))
            cafes.append(len(pois_temp[pois_temp['amenity']=='cafe'].dropna(axis=1, how='any')))
            unis.append(len(pois_temp[pois_temp['amenity']=='university'].dropna(axis=1, how='any')))
        else:
            restaurants.append(0)  # if len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')) > 0 else restaurants.append(0) 
            bars.append(0)
            cafes.append(0)
            unis.append(0)
    data_temp['restaurants'] = restaurants 
    data_temp['bars'] = bars 
    data_temp['cafes'] = cafes
    data_temp['universities'] = unis
    data_new = data_temp
    return data_new


def pois_subway(dataset):
    tags = {'railway': 'subway'}
    cta = []
    data_temp = dataset
    for x in range(len(data_temp)):
        pois_temp = ox.pois_from_point(point=(data_temp.latitude.iloc[x],data_temp.longitude.iloc[x]), dist=1000, tags=tags)  
        if 'subway' in pois_temp:
            train = pois_temp[pois_temp['subway'] == 'yes'].dropna(axis=1, how='any')
            cta.append((len(train['name'].unique())))
        else:
            cta.append(0)
    #print(len(restaurants))
    data_temp['CTA'] = cta
    data_cta = data_temp
    return data_cta

def main():
    dataset = choose_csv()
    data_amenities = pois_amenities(dataset)
    data_amenities_sub = pois_subway(data_amenities)
    return data_amenities_sub

data_with_counts = main()
data_with_counts.to_csv('data_with_counts.csv')


    