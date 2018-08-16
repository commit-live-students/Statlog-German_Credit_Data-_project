<<<<<<< HEAD
import sys, os
=======
>>>>>>> 909c0ea60336b196926e226307816947a629d970
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE
from greyatomlib.statlog_german_credit_data_project.q05_split.build import q05_split, q03_encode_features, q01_load_data_and_add_column_names
path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
X_train, X_test, y_train,y_test= q05_split(data)

<<<<<<< HEAD
=======
    
    
>>>>>>> 909c0ea60336b196926e226307816947a629d970
