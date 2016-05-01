import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset_100k.csv'
df = pd.read_csv(data_path)
df = df.dropna()


mask = df.tip_amount>=10
plt.figure(figsize=(20,15),frameon = 0)
ax = plt.gca()
ax.set_axis_bgcolor('black')
x1 = df.pickup_longitude.tolist()
x2 = df.dropoff_longitude.tolist()
y1 = df.pickup_latitude.tolist()
y2 = df.dropoff_latitude.tolist()

ax.scatter(x1+x2,y1+y2,color = 'w',s=.01,marker = 'o',alpha = 0.4)


x1 = df[mask].pickup_longitude.tolist()
x2 = df[mask].dropoff_longitude.tolist()
y1 = df[mask].pickup_latitude.tolist()
y2 = df[mask].dropoff_latitude.tolist()

ax.scatter(x1,y1,color = 'b',s=.19,marker = 'x',alpha = 0.9)
ax.scatter(x2,y2,color = 'r',s=.19,marker = 'x',alpha = 0.9)
# plt.title('Tip Amount >= $10.00')
plt.xlim((-74.06,-73.77))
plt.ylim((40.56,40.91))
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
ax.axes.get_xaxis().set_visible(0)
ax.axes.get_yaxis().set_visible(0)
plt.show()
