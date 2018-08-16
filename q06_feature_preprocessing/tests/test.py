from unittest import TestCase
from ..build import q06_feature_preprocessing,q05_split, q03_encode_features,  q01_load_data_and_add_column_names
from inspect import getfullargspec

path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
X_train, X_test, y_train,y_test= q05_split(data)
df = q06_feature_preprocessing(X_train, X_test, y_train,y_test,0,8)


class Test_feature_preprocessing(TestCase):
     def test_args(self):
        arg = getfullargspec(q06_feature_preprocessing).args
        self.assertEqual(len(arg), 6, "Expected argument(s) %d, Given %d" % (6, len(arg)))

   
     def test_return_train(self):
        self.assertEqual(df[0].shape, (972, 8), "The Expected return type do not match with the return type")

     def test_return_test(self):
        self.assertEqual(df[1].shape, (300, 8), "The Expected return type do not match with the return type")
