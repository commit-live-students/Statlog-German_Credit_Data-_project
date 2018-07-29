# %load q02_plot_all_variable/build.py
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
    num = df.select_dtypes(['int64']).columns
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            plt.plot(df[num[i]],df[num[j]])
    plt.show()

