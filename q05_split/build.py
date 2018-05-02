# %load q05_split/build.py
import sys, os
from sklearn.model_selection import train_test_split
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q05_split(path,test_size = 0.2,random_state=9):
    data,data_dict = q03_encode_features(path)
    Y = data['good/bad']
    X = data.iloc[:,:-1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)
    return X_train[1:], X_test, y_train[1:], y_test






