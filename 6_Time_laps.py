import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv'
df = pd.read_csv(data_path)
df = df.dropna()
x_for_km = df.trip_distance/(df.trip_time_in_secs.astype(float)/3600)
x_for_km = x_for_km.map(lambda x: np.nan if x<=0 else x)
x_for_km = x_for_km.replace([np.nan,np.inf], 0)
df['trip_speed']= x_for_km

df['pickup_dt'] = df.pickup_datetime.map(pd.to_datetime)
df['pickup_hour'] = df.pickup_dt.dt.hour

mask_low = (df.trip_speed<=25)
mask_med = (df.trip_speed>25)&(df.trip_speed<=45)
mask_high = (df.trip_speed>45)
for hour in set(df.pickup_hour):
    mask_low = (df.trip_speed<=25) & (df.pickup_hour==hour)
    mask_med = (df.trip_speed>25)&(df.trip_speed<=45) & (df.pickup_hour==hour)
    mask_high = (df.trip_speed>45) & (df.pickup_hour==hour)
    ''' White Background'''
    plt.figure(figsize=(20,15),frameon = 0)
    ax = plt.gca()
    ax.set_axis_bgcolor('black')
    x1 = df.pickup_longitude.tolist()
    x2 = df.dropoff_longitude.tolist()
    y1 = df.pickup_latitude.tolist()
    y2 = df.dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'w',s=.01,marker = 'o',alpha = 0.7)
    ''' Mask Low Speed'''

    x1 = df[mask_low].pickup_longitude.tolist()
    x2 = df[mask_low].dropoff_longitude.tolist()
    y1 = df[mask_low].pickup_latitude.tolist()
    y2 = df[mask_low].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'b',s=.04,marker = 'o',alpha = 0.4)


    '''Mask Med Speed'''
    x1 = df[mask_med].pickup_longitude.tolist()
    x2 = df[mask_med].dropoff_longitude.tolist()
    y1 = df[mask_med].pickup_latitude.tolist()
    y2 = df[mask_med].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'y',s=1,marker = 'o',alpha = 0.9)


    '''Mask High Speed'''
    x1 = df[mask_high].pickup_longitude.tolist()
    x2 = df[mask_high].dropoff_longitude.tolist()
    y1 = df[mask_high].pickup_latitude.tolist()
    y2 = df[mask_high].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'r',s=1,marker = 'o',alpha = 0.9)


    plt.xlim((-74.06,-73.77))
    plt.ylim((40.61,40.91))
    plt.xlim((-74.06,-73.77))
    plt.ylim((40.56,40.91))
    # plt.xlabel('Longitude')
    # plt.ylabel('Latitude')
    plt.title('Pickup Hour %d'%hour)
    ax.axes.get_xaxis().set_visible(0)
    ax.axes.get_yaxis().set_visible(0)
    print hour
    path = 'Hour %d'%hour
    plt.savefig(path)
