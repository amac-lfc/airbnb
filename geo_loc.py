import pandas as pd
import numpy as np 
### packages for spatial analysis 
import osmnx as ox   # for finding objects within a given radius 
import openrouteservice as ors   # for finding the walking distance in seconds and meters to a given point 
### for promting to choose a file 
from tqdm import tqdm
from progressbar import ProgressBar
### others 
import re
import requests
import time

### for ors we need an API Key, it can be found on the https://openrouteservice.org/ once you create an account 
client = ors.Client(key='5b3ce3597851110001cf6248fb1ecfcd8ab8422b93b5dd978d83e93e')
ox.config(log_console=False, use_cache=True)
file_name = input('Enter the name of your CSV file (Leave empty for main dataset): ') 
if not file_name:
    file_name = 'listings_cleaned.csv'
print('CSV File Name: {}'.format(file_name))
time.sleep(1)

def choose_csv(main_data = file_name):
    '''
    Returns the dataset you chose. 

    Returns:
        data: a Pandas DataFrame object
    '''


    if main_data != None:
        data = pd.read_csv(file_name,index_col=['id'])
    else:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        data = pd.read_csv(filename)
    return data

def pois_amenities(data):
    '''
    Returns a new extended dataset with the number of restaurants, 
    bars, cafes, and university campuses within a radius of 1000 meters (0.6 miles). 

    Parameters:
        data: The dataset you chose (is passed from `choose_csv()` function)

    Returns:
        data_new: The extended dataframe `data`
    '''
    tags = {'amenity':['restaurant', 'bar', 'cafe','university']} # here we specify the POIs (Points of Interest) we want to find 
    restaurants = []
    bars = []
    cafes = []
    unis = []
    data_temp = data 
    for x in tqdm(range(len(data_temp)),desc='Amenities'):
        pois_temp = ox.pois_from_point(point=(data_temp.latitude.iloc[x],data_temp.longitude.iloc[x]), dist=1000, tags=tags)  #get POIs (tags) for a point with latitude and longitude in a range dist (in meters) 
        # pois_temp is a DataFrame with the information about each POI 
        if 'amenity' in pois_temp: 
            '''
            Adding the number of POIs to corresponding arrays
            '''
            if len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')) > 0:
                restaurants.append(len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')))  
            else: 
                restaurants.append(0)
            if len(pois_temp[pois_temp['amenity']=='bar'].dropna(axis=1, how='any')) > 0:
                bars.append(len(pois_temp[pois_temp['amenity']=='bar'].dropna(axis=1, how='any'))) 
            else: 
                bars.append(0)
            if len(pois_temp[pois_temp['amenity']=='cafe'].dropna(axis=1, how='any')) > 0:
                cafes.append(len(pois_temp[pois_temp['amenity']=='cafe'].dropna(axis=1, how='any'))) 
            else: 
                cafes.append(0)   
            if len(pois_temp[pois_temp['amenity']=='university'].dropna(axis=1, how='any')) > 0:
                unis.append(len(pois_temp[pois_temp['amenity']=='university'].dropna(axis=1, how='any'))) 
            else:
                 unis.append(0)      
        else:
            restaurants.append(0)  # if len(pois_temp[pois_temp['amenity']=='restaurant'].dropna(axis=1, how='any')) > 0 else restaurants.append(0) 
            bars.append(0)
            cafes.append(0)
            unis.append(0)
    '''
    Appending the gathered counts to a new dataframe (extending the initial one) 
    '''
    data_temp['restaurants'] = restaurants 
    data_temp['bars'] = bars 
    data_temp['cafes'] = cafes
    data_temp['universities'] = unis
    data_new = data_temp
    return data_new


def pois_subway(data):
    '''
    Returns a new extended dataset with the number of subway (in case of Chicago CTA) 
    stations within a radius of 1000 meters as well as the walking time to the nearest one in seconds.
    If there are not any stations in the radius of 1000m, the walking time to a station within a radius of 5000m is checked.  
    '''
       
    tags = {'railway': 'subway'}
    cta = []
    walk_time = [] #walking time to the closest CTA station in seconds 
    data_temp = data
    # for i in tqdm(range(len(data_temp))):
    for x in tqdm(range(len(data_temp)), desc = 'Subway'):
        pois_temp = ox.pois_from_point(point=(data_temp.latitude.iloc[x],data_temp.longitude.iloc[x]), dist=1000, tags=tags)  
        if 'subway' in pois_temp and len(pois_temp[pois_temp['subway'] == 'yes'].dropna(axis=1, how='any')) > 0: # if there is a column 'subway' in the temporary dataset with POIs for a listing x it means that there are stations within 1000m
            train = pois_temp[pois_temp['subway'] == 'yes'].dropna(axis=1, how='any') # slicing out the information about the subways stations (name and location)
            cta.append((len(train['name'].unique()))) # adding the number of unique CTA stations (.unique because several entrences to the same station are recorded)
            coordinates = [[data_temp.iloc[x].longitude,data_temp.iloc[x].latitude]] # extracting the long and lat of a listing x 
            '''
            The following function uses regular expressions (import re) to format the long and lat 
            retrieved by the ox.pois_from_point method. It drops all the symbols that are not a number (^0-9), not a dot (^.), not a space (^ ), and not a negative sign (^-) 
            ''' 
            for x in range (len(train)):
                loc_str = str(train.geometry.iloc[x])
                loc_num = re.sub("[^0-9,^.,^ ,-]", "", loc_str).lstrip().split(' ')
                for i in range(len(loc_num)): 
                    loc_num[i] = float(loc_num[i]) 
                coordinates.append(loc_num)
            '''
            Read more about the OpenRouteService in their docs: https://openrouteservice-py.readthedocs.io/en/latest/ 
            locations - a dicitonary with the pairs of long and lat (includes both the starting point and destination(s))
            destinations - a list of indecies of point to which the distance is going to be measured (basicly just excludes the starting point)
            profile - method of moving (some of the alternatives are “driving-car” and  “cycling-regular”)
            metrics - 'duration': time in secodnds to destination
            also - 'distance': distance in meters  
            
            '''
            matrix = client.distance_matrix(
                locations = coordinates,
                destinations = [_ for _ in range(1,len(coordinates))],
                profile = 'foot-walking',
                metrics = ['duration'],
                validate = False,
            )
            walk_time.append(round((matrix['durations'][0][matrix['durations'][0].index(min(matrix['durations'][0]))]/60),2))
        else:
            cta.append(np.nan) 
            pois_temp = ox.pois_from_point(point=(data_temp.latitude.iloc[x],data_temp.longitude.iloc[x]), dist=5000, tags=tags)  
            train = pois_temp[pois_temp['subway'] == 'yes'].dropna(axis=1, how='any')
            coordinates = [[data_temp.iloc[x].longitude,data_temp.iloc[x].latitude]]
            for x in range (len(train)):
                loc_str = str(train.geometry.iloc[x])
                loc_num = re.sub("[^0-9,^.,^ ,-]", "", loc_str).lstrip().split(' ')
                for i in range(len(loc_num)): 
                    loc_num[i] = float(loc_num[i]) 
            coordinates.append(loc_num)
            matrix = client.distance_matrix(
                locations = coordinates,
                destinations = [_ for _ in range(1,len(coordinates))],
                profile = 'foot-walking',
                metrics = ['distance', 'duration'],
                validate = False,
            )
            walk_time.append(round((matrix['durations'][0][matrix['durations'][0].index(min(matrix['durations'][0]))]/60),2))
    data_temp['cta'] = cta
    data_temp['time_to_cta_minutes'] = walk_time
    data_cta = data_temp
    return data_cta

def save_csv(dataframe):
    data_with_counts = dataframe
    #print(data_with_counts.head(10))
    data_with_counts.to_csv('data_with_counts_'+str(len(data_with_counts))+'.csv')


if __name__ == "__main__":
    start = time.time()
    dataset = choose_csv(main_data = 'listings_cleaned.csv')
    data_amenities = pois_amenities(dataset)
    new_data = pois_subway(data_amenities)
    end = time.time()
    save_csv(new_data)
    print(end - start)



    