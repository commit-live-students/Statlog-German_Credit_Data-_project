import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
#plt.switch_backend('agg')
import sys, os
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
from greyatomlib.statlog_german_credit_data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q04_correlation_plot(path):
    a = q01_load_data_and_add_column_names(path)
    df_corr = a.corr()
    df_corr.plot(kind='hist')
    
    













