import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')
import sys, os
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q04_correlation_plot(path):
    df = q03_encode_features(path)[0]
    corr1 = df.corr()
    sns.heatmap(corr1)
    plt.show()

q04_correlation_plot(path)
