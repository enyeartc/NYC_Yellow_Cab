import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def plot_trip_speed(df):
    df = df.dropna()
    x_for_km = df.trip_distance/(df.trip_time_in_secs.astype(float)/3600)
    x_for_km = x_for_km.map(lambda x: np.nan if x<=0 else x)
    x_for_km = x_for_km.replace([np.nan,np.inf], 0)
    df['trip_speed']= x_for_km
    x_for_km = x_for_km[(x_for_km<100)&(x_for_km>0.0)]
    x_for_km = x_for_km.reshape(-1,1)
    km = KMeans(7,n_jobs = -1,max_iter=500)
    km.fit(x_for_km)

    print km.cluster_centers_
    '''
    15.87
    8.78
    27.95
    20.86
    12.079
    38.425
    5.2898
    71.055
    '''
    mask_low = (df.trip_speed<=25)
    mask_med = (df.trip_speed>25)&(df.trip_speed<=45)
    mask_high = (df.trip_speed>45)

    ''' Mask Low Speed'''
    plt.figure(figsize=(20,15),frameon = 0)
    ax = plt.gca()
    ax.set_axis_bgcolor('black')
    x1 = df[mask_low].pickup_longitude.tolist()
    x2 = df[mask_low].dropoff_longitude.tolist()
    y1 = df[mask_low].pickup_latitude.tolist()
    y2 = df[mask_low].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'b',s=.01,marker = 'o',alpha = 0.4)


    '''Mask Med Speed'''
    x1 = df[mask_med].pickup_longitude.tolist()
    x2 = df[mask_med].dropoff_longitude.tolist()
    y1 = df[mask_med].pickup_latitude.tolist()
    y2 = df[mask_med].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'y',s=.1,marker = 'o',alpha = 0.4)


    '''Mask High Speed'''
    x1 = df[mask_high].pickup_longitude.tolist()
    x2 = df[mask_high].dropoff_longitude.tolist()
    y1 = df[mask_high].pickup_latitude.tolist()
    y2 = df[mask_high].dropoff_latitude.tolist()

    ax.scatter(x1+x2,y1+y2,color = 'r',s=.1,marker = 'o',alpha = 0.4)


    plt.xlim((-74.06,-73.77))
    plt.ylim((40.61,40.91))
    plt.xlim((-74.06,-73.77))
    plt.ylim((40.56,40.91))
    # plt.xlabel('Longitude')
    # plt.ylabel('Latitude')
    # plt.title('Average Trip Speed')
    ax.axes.get_xaxis().set_visible(0)
    ax.axes.get_yaxis().set_visible(0)

    ''' plot cluster colors '''
    df['speed_cluster'] = km.predict(df.trip_speed.reshape(len(df),-1))
    plt.figure(figsize=(20,15),frameon = 0)
    ax = plt.gca()
    ax.set_axis_bgcolor('black')
    c = ['b','g','r','c','m','y','w']
    k = set(df.speed_cluster)
    for col,clus in zip(c[0:len(k)],k):
        mask = (df.speed_cluster ==clus)
        x1 = df[mask].pickup_longitude.tolist()
        x2 = df[mask].dropoff_longitude.tolist()
        y1 = df[mask].pickup_latitude.tolist()
        y2 = df[mask].dropoff_latitude.tolist()
        ax.scatter(x1+x2,y1+y2,color = col,s=.1,marker = 'o',alpha = 0.4)
        plt.xlim((-74.06,-73.77))
        plt.ylim((40.61,40.91))
        plt.xlim((-74.06,-73.77))
        plt.ylim((40.56,40.91))
        # plt.xlabel('Longitude')
        # plt.ylabel('Latitude')
        # plt.title('Average Trip Speed')
        ax.axes.get_xaxis().set_visible(0)
        ax.axes.get_yaxis().set_visible(0)
    plt.show()

if __name__ == '__main__':
    data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv'
    df = pd.read_csv(data_path)
    plot_trip_speed(df)
