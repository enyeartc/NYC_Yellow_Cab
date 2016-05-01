
import pandas as pd
import numpy as np

'''
Clean and Subset data
'''

sub_sample_size= 150000 #create subset of all files

def clean_and_subset(x):
    df = pd.read_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_'+str(x+1)+'.csv')
    df.dropna(inplace = 1)
    df.reset_index(inplace = 1)
    pickup_mask = (df.pickup_latitude<42)&(df.pickup_latitude>40)&(df.pickup_longitude<-70)&(df.pickup_longitude>-76)
    dropoff_mask = (df.dropoff_latitude<42)&(df.dropoff_latitude>40)&(df.dropoff_longitude<-70)&(df.dropoff_longitude>-76)
    passenger_mask = df.passenger_count<15
    trip_time_mask = (df.trip_time_in_secs/3600.0 < 24)&(df.trip_time_in_secs>0)
    trip_miles_mask = (df.trip_distance > 0)&(df.trip_distance<(24*75))

    df.drop(['store_and_fwd_flag','index'],axis=1,inplace = 1)

    df = df[pickup_mask&dropoff_mask&passenger_mask&trip_time_mask&trip_miles_mask]

    df.to_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_'+str(x+1)+'.csv',index=0,index_label=0)

    length = len(df)
    subset_mask = np.random.choice(xrange(0,length),sub_sample_size,replace = 0)
    subset_mask.sort()
    if x == 0:
        df_sub = df.ix[subset_mask].copy()
        df_sub.to_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv',index=0,index_label=0)
    else:
        df_sub = pd.read_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv')
        df_sub = pd.concat([df_sub,df.ix[subset_mask].copy()])
        df_sub.to_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv',index=0,index_label=0)
    %reset_selective -f df_sub df

if __name__ == '__main__':
    for x in range(0,12):
        clean_and_subset(x)
