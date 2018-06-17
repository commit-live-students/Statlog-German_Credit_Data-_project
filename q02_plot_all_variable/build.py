import pandas as pd
import numpy as np
import sys, os
from math import ceil
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.statlog_german_credit_data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q02_plot_all_variable(path,d=5):
    df = q01_load_data_and_add_column_names(path)
    num = ['int16','int32','int64','float16','float32','float64']
    num_features = list(df.select_dtypes(num).columns)
    cat_features = list(set(list(df.columns)) - set(num_features))
    for i in range(0,len(num_features)):
        for j in range(i+1,len(num_features)):
            plt.subplot(4,5,i+1)
            plt.plot(df[num_features[i]],df[num_features[j]])
    plt.show()

#q02_plot_all_variable(path)
