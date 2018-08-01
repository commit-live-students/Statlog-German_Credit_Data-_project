import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from greyatomlib.statlog_german_credit_data_project.q06_feature_preprocessing.build import q06_feature_preprocessing, q05_split,q03_encode_features, q01_load_data_and_add_column_names

path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
X_train,X_test,y_train,y_test=q05_split(data)
X_train,X_test,y_train,y_test=q06_feature_preprocessing(X_train,X_test,y_train,y_test,0,8)

    
