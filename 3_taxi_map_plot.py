import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_1.csv'
df = pd.read_csv(data_path)


plt.figure(figsize=(20,15),frameon = 0)
ax = plt.gca()
ax.set_axis_bgcolor('black')
# x1 = df.pickup_longitude.tolist()
x2 = df.dropoff_longitude.tolist()
# y1 = df.pickup_latitude.tolist()
y2 = df.dropoff_latitude.tolist()

# ax.scatter(x1,y1,color = 'w',s=.01,marker = '.',alpha = 0.2)
ax.scatter(x2,y2,color = 'w',s=.01,marker = 'o',alpha = 0.2)
ax.axes.get_xaxis().set_visible(0)
ax.axes.get_yaxis().set_visible(0)
plt.xlim((-74.06,-73.77))
plt.ylim((40.56,40.91))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('New York City Map of Taxi Drop-off Locations, 17 Million Data Points')
plt.show()
