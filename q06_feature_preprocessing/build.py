import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE
from greyatomlib.statlog_german_credit_data_project.q05_split.build import q05_split
path = 'data/GermanData.csv'
import pandas as pd

def q06_feature_preprocessing(path,kind='regular',random_state=9,k=8):
    X_train,X_test,y_train,y_test = q05_split(path,test_size=0.2,random_state=random_state)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)
    sm = SMOTE(random_state=random_state,kind=kind)
    X_res, y_res = sm.fit_sample(X_train,y_train)
    skbest = SelectKBest(k=k)
    X_train_final = pd.DataFrame(skbest.fit_transform(X_res,y_res))
    ind = skbest.get_support()
    X_test = pd.DataFrame(X_test)
    X_test = X_test.loc[:,ind]
    return X_train_final,X_test,y_res,y_test

#q06_feature_preprocessing(path,kind='regular',random_state=9,k=8)
