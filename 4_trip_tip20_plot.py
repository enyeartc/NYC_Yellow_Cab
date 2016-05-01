import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def plot_tips(df):
    df = df.dropna()
    x_for_km = df.tip_amount/df.fare_amount.astype(float)
    x_for_km = x_for_km.replace([np.inf,np.nan], 0)
    x_for_km = x_for_km.reshape(-1,1)
    km = KMeans(3,n_jobs = -1,max_iter=500)
    km.fit(x_for_km*100)
    df_nTip = df[x_for_km == 0]
    df_tl20 = df[x_for_km < 0.2]
    df_tg20 = df[x_for_km >= 0.2]

    ''' 20% Pickup Tips'''
    plt.figure(figsize=(20,15),frameon = 0)
    ax = plt.gca()
    ax.set_axis_bgcolor('black')
    x1 = df.pickup_longitude.tolist()
    x2 = df.dropoff_longitude.tolist()
    y1 = df.pickup_latitude.tolist()
    y2 = df.dropoff_latitude.tolist()

    ax.scatter(x1,y1,color = 'w',s=.01,marker = 'o',alpha = 0.4)
    ax.scatter(x2,y2,color = 'w',s=.01,marker = 'o',alpha = 0.4)

    plt.xlim((-74.06,-73.77))
    plt.ylim((40.61,40.91))


    x_tg20 = df_tg20.pickup_longitude.tolist()
    y_tg20 = df_tg20.pickup_latitude.tolist()

    # ax.scatter(x_nTip,y_nTip,color = 'b',s=1,marker = 'o',alpha = 0.4)
    # ax.scatter(x_tl20,y_tl20,color = 'g',s=.05,marker = 'o',alpha = 0.4)
    ax.scatter(x_tg20,y_tg20,color = 'b',s=.01,marker = 'o',alpha = 0.6)

    plt.xlim((-74.06,-73.77))
    plt.ylim((40.56,40.91))
    # plt.title('Tips Greater Than Equal to 20% at Pickup Location')
    # plt.xlabel('Longitude')
    # plt.ylabel('Latitude')
    ax.axes.get_xaxis().set_visible(0)
    ax.axes.get_yaxis().set_visible(0)
    # plt.savefig('20%_pickup')


    '''20% Destination Tips'''
    plt.figure(figsize=(20,15),frameon = 0)
    ax = plt.gca()
    ax.set_axis_bgcolor('black')
    x1 = df.pickup_longitude.tolist()
    x2 = df.dropoff_longitude.tolist()
    y1 = df.pickup_latitude.tolist()
    y2 = df.dropoff_latitude.tolist()

    ax.scatter(x1,y1,color = 'w',s=.01,marker = 'o',alpha = 0.4)
    ax.scatter(x2,y2,color = 'w',s=.01,marker = 'o',alpha = 0.4)

    plt.xlim((-74.06,-73.77))
    plt.ylim((40.61,40.91))

    x_tg20 = df_tg20.dropoff_longitude.tolist()
    y_tg20 = df_tg20.dropoff_latitude.tolist()


    # ax.scatter(x1,y1,color = 'r',s=.01,marker = 'o',alpha = 0.4)
    ax.scatter(x_tg20,y_tg20,color = 'b',s=.01,marker = 'o',alpha = 0.6)

    plt.xlim((-74.06,-73.77))
    plt.ylim((40.56,40.91))

    # plt.title('Tips Greater Than Equal to 20% at Drop-off Location')
    # plt.xlabel('Longitude')
    # plt.ylabel('Latitude')
    ax.axes.get_xaxis().set_visible(0)
    ax.axes.get_yaxis().set_visible(0)
    # plt.savefig('20%_pickup')
    plt.show()

if __name__ == '__main__':
    data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset_100k.csv'
    df = pd.read_csv(data_path)
    plot_tips(df)
