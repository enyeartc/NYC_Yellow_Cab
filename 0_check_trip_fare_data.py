import pandas as pd

'''
Function checks the two parts of data alignment, so that they can be concateded 
'''

trip_data = ['trip_data_1.csv',
'trip_data_2.csv',
'trip_data_3.csv',
'trip_data_4.csv',
'trip_data_5.csv',
'trip_data_6.csv',
'trip_data_7.csv',
'trip_data_8.csv',
'trip_data_9.csv',
'trip_data_10.csv',
'trip_data_11.csv',
'trip_data_12.csv']

trip_fare = ['trip_fare_1.csv',
'trip_fare_2.csv',
'trip_fare_3.csv',
'trip_fare_4.csv',
'trip_fare_5.csv',
'trip_fare_6.csv',
'trip_fare_7.csv',
'trip_fare_8.csv',
'trip_fare_9.csv',
'trip_fare_10.csv',
'trip_fare_11.csv',
'trip_fare_12.csv']

def check_trip_fare_data(num):
    df1 = pd.read_csv('G:\\taxi_data\\'+trip_data[num])
    df1.columns = df1.columns.map(lambda x:x.replace(' ',''))
    df2 = pd.read_csv('G:\\taxi_data\\'+trip_data[num])
    df2.columns = df2.columns.map(lambda x:x.replace(' ',''))
    df1 = df1.dropna()
    df2 = df2.dropna()
    n = sum(df1.pickup_datetime == df2.pickup_datetime)
    print num+1, n/float(df1.pickup_datetime.count())


for x in range(0,12):
    check_trip_fare_data(x)
