import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from greyatomlib.statlog_german_credit_data_project.q06_feature_preprocessing.build import q06_feature_preprocessing

path = 'data/GermanData.csv'

def q07_randomsearch_predict(path):
    X_train,X_test,y_train,y_test = q06_feature_preprocessing(path,kind='regular',random_state=9,k=8)
    param_distributions = {'n_estimators':[100,150,200],'max_depth':[3,4,5],'min_samples_split':[2,3,4]}
    model = GradientBoostingClassifier()
    search = RandomizedSearchCV(model,param_distributions)
    search.fit(X_train,y_train)
    y_pred = search.predict(X_test)
    auc_score = roc_auc_score(y_test,y_pred)
    return auc_score

#q07_randomsearch_predict(path)
