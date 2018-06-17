import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
from greyatomlib.statlog_german_credit_data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q03_encode_features(path):
    df = q01_load_data_and_add_column_names(path)
    df1 = df.iloc[1:,:].copy(deep=True)
    d = {}
    i = 0
    le = LabelEncoder()
    for val in list(df.columns):
        if df[val].dtype == 'object':
            d[i] = val
            df1[val] = le.fit_transform(df1[val])
            i = i + 1

    return df1,d

#q03_encode_features(path)
