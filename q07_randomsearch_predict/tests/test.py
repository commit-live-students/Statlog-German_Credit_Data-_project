import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_randomsearch_predict, q06_feature_preprocessing, q05_split,q03_encode_features, q01_load_data_and_add_column_names
from inspect import getfullargspec


path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
X_train,X_test,y_train,y_test=q05_split(data)
X_train,X_test,y_train,y_test=q06_feature_preprocessing(X_train,X_test,y_train,y_test,0,8)
score=q07_randomsearch_predict(X_train,X_test,y_train,y_test)

class Test_randomsearch_predict(TestCase):
    def test_args(self):
        arg = getfullargspec(q07_randomsearch_predict).args
        self.assertEqual(len(arg), 4, "Expected argument(s) %d, Given %d" % (4, len(arg)))


    def test_return_train(self):
        self.assertGreaterEqual(score, 0.63, "The Expected return type do not match with the return type")

