import pandas as pd
import numpy as np
from haversine import haversine
import time
from math import radians, sin, cos, asin, sqrt, pi, atan2

def haversine2(needle, haystack):
    """needle is a single (lat,long) tuple.
        haystack is a numpy array to find the point in
        that has the shortest distance to needle
    """
    if type(haystack) == tuple:
        haystack = np.array(haystack).reshape(-1,len(haystack))
    else:
        needle = np.array(needle).reshape(len(needle),-1)
        haystack = np.array(haystack).reshape(len(haystack),-1)
    earth_radius_miles = 6371*0.621371
    dlat = np.radians(haystack[:,0]) - radians(needle[0])
    dlon = np.radians(haystack[:,1]) - radians(needle[1])
    a = np.square(np.sin(dlat/2.0)) + cos(radians(needle[0])) * np.cos(np.radians(haystack[:,0])) * np.square(np.sin(dlon/2.0))
    # great_circle_distance = 2 * np.arcsin(np.minimum(np.sqrt(a), np.repeat(1, len(a))))
    d = 2*earth_radius_miles * np.arcsin(np.sqrt(a))
    return d

def similar_cluster(df,miles = 0.1):
    clusters = {}
    cNum = 0
    already_clustered = set()
    plat = df['pickup_latitude']
    plon = df['pickup_longitude']
    dlat = df['dropoff_latitude']
    dlon = df['dropoff_longitude']
    index = len(plat)
    for x in xrange(0,index-1):
        if x not in already_clustered:
            index2 = range(x+1,index)
            pdist = haversine2((plat[x],plon[x]),zip(plat[index2],plon[index2]))
            pdist = zip(pdist,index2)
            index2 = [data[1] for data in pdist if data[0]<=miles ]

            if index2 == []:
                continue
            ddist = haversine2((dlat[x],dlon[x]),zip(dlat[index2],dlon[index2]))
            for cnt, y in enumerate(index2):
                if y not in already_clustered:
                    if ddist[cnt]<=miles:
                        # print 'distances:',pdist[cnt],ddist[cnt]
                        if cNum in clusters:
                            clusters[cNum]+=[y]
                            already_clustered.add(y)
                        else:
                            clusters.update({cNum:[x,y]})
                            already_clustered.add(y)
                            print x/float(index),cNum

        if cNum in clusters:
            cNum +=1
    return clusters


def bad_driver(df,data,cheat_miles=2,time_inc = 1):
    bad_drivers = 0
    bad_driver_ids = []
    dist_amount = []
    trip_time = []
    for d in data:
        dist = df.ix[data[d],8].tolist()
        time = df.ix[data[d],7].tolist()
        ids = df.ix[data[d],1].tolist()
        mdist = min(dist)
        mtime = sum(time)/float(len(time))
        for cnt, m in enumerate(dist):
            if ((m-mdist >= cheat_miles) and (time[cnt]-(mtime*time_inc)>0)):
                bad_drivers += 1
                bad_driver_ids.append(ids[cnt])
                dist_amount.append(m-mdist)
                trip_time.append(time[cnt])
    return bad_drivers, bad_driver_ids, dist_amount, trip_time

if __name__ == '__main__':
    data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv'
    df = pd.read_csv(data_path)
    data = similar_cluster(df.head(400000))
    a,b,c,d = bad_drivers(df,data)
