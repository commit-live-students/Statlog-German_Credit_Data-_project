import sys, os
from sklearn.model_selection import train_test_split
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q05_split(path,test_size=0.2,random_state=9):
    df = q03_encode_features(path)[0]
    X = df.iloc[1:,:-1]
    y = df.iloc[1:,-1]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)
    return X_train,X_test,y_train,y_test
#q05_split(path)
