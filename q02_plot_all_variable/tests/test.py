import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_plot_all_variable, q01_load_data_and_add_column_names
from inspect import getfullargspec

path = './data/GermanData.csv'
data = q01_load_data_and_add_column_names(path)   
q02_plot_all_variable(data)


class Test_plot_all_features(TestCase):
    def test_args(self):
        arg = getfullargspec(q02_plot_all_variable).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

