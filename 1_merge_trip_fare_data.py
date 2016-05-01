import pandas as pd

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

def load_merge_data(num):
    df1 = pd.read_csv('G:\\taxi_data\\'+trip_data[num])
    df1.columns = df1.columns.map(lambda x:x.replace(' ',''))
    df2 = pd.read_csv('G:\\taxi_data\\'+trip_fare[num])
    df2.columns = df2.columns.map(lambda x:x.replace(' ',''))
    df2.drop(['medallion','hack_license','vendor_id','pickup_datetime'],axis = 1,inplace = 1)
    new_df = pd.concat([df1,df2],axis = 1)
    new_df.to_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_'+str(num+1)+'.csv',index=0,index_label=0)
    return None

for x in range(0,12):
    load_merge_data(x)
