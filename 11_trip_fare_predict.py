import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.grid_search import GridSearchCV
from haversine import haversine

data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv'
df = pd.read_csv(data_path)

df['pickup_dt'] = df.pickup_datetime.map(pd.to_datetime)
df['pickup_dow'] = df.pickup_dt.dt.dayofweek
df['pickup_hour'] = df.pickup_dt.dt.hour
df['pickup_month'] = df.pickup_dt.dt.month
dist = []
for ind in xrange(len(df)):
    dist.append(haversine((df.pickup_latitude[ind],df.pickup_longitude[ind]),(df.dropoff_latitude[ind],df.dropoff_longitude[ind])))
df['geo_dist'] = dist
df = pd.get_dummies(df,columns = ['vendor_id','rate_code','payment_type','pickup_dow','pickup_hour','pickup_month'])
df.drop(['tip_amount','total_amount','pickup_datetime','pickup_dt','dropoff_datetime','hack_license','medallion','trip_time_in_secs','trip_distance'],axis = 1,inplace = 1)
df.dropna(inplace = 1)
# df.to_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset_rf.csv',index=0,index_label=0)
# %reset_selective -f df subset_mask length data_path
# df = pd.read_csv('C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset_rf.csv')
y = df.pop('fare_amount').values
x = df.values

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.33, random_state = 42)

random_forest_grid = {'n_estimators': [10],'n_jobs' : [-1]} #,
                        # 'criterion': ['gini','entropy'],
                        # 'min_samples_split': [4,5,6],
                        # 'min_samples_leaf': [1,2],
                        # 'n_jobs': [-1],
                        # 'max_features': [None],
                        # 'class_weight': ['balanced']}

rf_gridsearch = GridSearchCV(RandomForestRegressor(),
                             random_forest_grid,
                             n_jobs=-1,
                             verbose=True,
                             cv=3)

rf_gridsearch.fit(X_train, y_train)

print "best parameters:", rf_gridsearch.best_params_

best_rf_model = rf_gridsearch.best_estimator_

y_pred = best_rf_model.predict(X_test)

print "Accuracy with best rf:", cross_val_score(best_rf_model, X_test, y_test).mean()

rf = RandomForestRegressor(n_estimators=10, oob_score=True,n_jobs = -1)

print "Accuracy with default param rf:", cross_val_score(rf, X_test, y_test).mean()



futures = zip(df.columns.tolist(),best_rf_model.feature_importances_)
futures.sort(key = lambda x:x[1],reverse = 1)
labels = []
fracs = []
total = 0
for f,v in futures:
    if total < .90:
        print f,v
        labels.append(f)
        fracs.append(v)
        total += v
fracs.append(1-sum(fracs))
explode = [0]*len(fracs)
explode[-1] = 0.1
figure(1,figsize=(6,6),frameon = 0)
colors = ['royalblue','g','m','c','violet','darkgray']
labels = ['Geo Dist','Rate Code 1','Dropoff Lon','Dropoff Lat','Pickup Lon','Features Left Off']
title('%1.1f%% Feature Importance'% (sum(fracs[:-1])*100))
pie(fracs, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90,colors = colors)
plt.show()
