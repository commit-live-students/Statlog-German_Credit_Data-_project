import pandas as pd 
import numpy as np
def q01_load_data_and_add_column_names(path):
    data=pd.read_csv(path,header=None,names=['account_status', 'month', 'credit_history', 'purpose', 'credit_amount', 'savings_account/bonds', 
    'employment', 'installment_rate', 'personal_status/sex', 'guarantors', 'residence_since', 
    'property', 'age', 'other_installment_plans', 'housing', 'number_of_existing_credits', 'job', 'liable', 'telephone', 'foreign_worker', 'good/bad'])

    data.loc[data['good/bad'] == 1, 'good/bad'] = 0
    data.loc[data['good/bad'] == 2, 'good/bad'] = 1
    return data 
credit=q01_load_data_and_add_column_names('./data/GermanData.csv')

