import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_split, q03_encode_features, q01_load_data_and_add_column_names

from inspect import getfullargspec

path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
df = q05_split(data, 0.3 ,0)


class Test_splits(TestCase):
      def test_args(self):
        arg = getargspec(q05_split).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

    def test_returns_X_train(self):
        self.assertEqual(df[0].shape, (700, 20), "The Expected return type do not match with the return type")

    def test_returns_X_test(self):
        self.assertEqual(df[1].shape, (300, 20), "The Expected return type do not match with the return type")

    def test_returns_y_train(self):
        self.assertIsInstance(df[2],pd.Series, "The Expected return type do not match with the return type")

    def test_returns_y_test(self):
        self.assertIsInstance(df[3],pd.Series, "The Expected return type do not match with the return type")


