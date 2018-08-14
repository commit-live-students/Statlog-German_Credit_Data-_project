import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from greyatomlib.statlog_german_credit_data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = './data/GermanData.csv'
data = q01_load_data_and_add_column_names(path)

