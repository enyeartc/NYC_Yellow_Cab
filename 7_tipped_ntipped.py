import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.grid_search import GridSearchCV
from pylab import *
import matplotlib.pyplot as plt
import seaborn as sns

'''
Determine Features for predicting tipped or not tipped
'''

def clean_prepare_data(df):
    df = pd.get_dummies(df,columns = ['vendor_id','rate_code','payment_type'])
    df.drop(['total_amount','pickup_datetime','dropoff_datetime','hack_license','medallion'],axis = 1,inplace = 1)
    df.dropna(inplace = 1)
    y = df.pop('tip_amount').values ==0
    x = df.values
    return x,y,df

def rf_cross_val(x,y):
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.33, random_state = 42)

    random_forest_grid = {'n_estimators': [100],'n_jobs': [-1]}

    rf_gridsearch = GridSearchCV(RandomForestClassifier(),
                                 random_forest_grid,
                                 n_jobs=-1,
                                 verbose=True,
                                 cv=3)

    rf_gridsearch.fit(X_train, y_train)

    print "best parameters:", rf_gridsearch.best_params_

    best_rf_model = rf_gridsearch.best_estimator_

    y_pred = best_rf_model.predict(X_test)

    print "Accuracy with best rf:", cross_val_score(best_rf_model, X_test, y_test).mean()

    rf = RandomForestClassifier(n_estimators=100, n_jobs = -1)

    print "Accuracy with default param rf:", cross_val_score(rf, X_test, y_test).mean()

    return best_rf_model

def plot_important_features(best_rf_model,df):
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
    labels=['Credit Card','Cash','Features Left Off']

    explode = [0,0,0.1]
    figure(1,figsize=(6,6),frameon = 0)
    title('%1.1f%% Feature Importance'% (sum(fracs[:-1])*100))
    pie(fracs, explode=explode, labels=labels,autopct='%1.1f%%', shadow=1, startangle=90,colors = ['royalblue','g','darkgray'])#
    plt.show()

if __name__ == '__main__':
    data_path = 'C:\\Users\\AVG\Documents\\Python\\taxi-data\\trip_fare_data_clean_subset.csv'
    df = pd.read_csv(data_path)
    x,y,df = clean_prepare_data(df)
    best_rf_model = rf_cross_val(x,y)
    plot_important_features(best_rf_model,df)
