import pandas as pd
import numpy as np


path = 'data/GermanData.csv'

def q01_load_data_and_add_column_names(path):
    data= pd.read_csv(filepath_or_buffer=path, skip_blank_lines=True #, header=None # commented to pass the testcase
            )
    data.columns =['account_status', 'month', 'credit_history', 'purpose', 'credit_amount', 'savings_account/bonds',
'employment', 'installment_rate', 'personal_status/sex', 'guarantors', 'residence_since',
'property', 'age', 'other_installment_plans', 'housing', 'number_of_existing_credits', 'job', 'liable', 'telephone', 'foreign_worker', 'good/bad'
                  ]
    #map good/bad to 0, 1
    data["good/bad"] = np.where( data["good/bad"]==1 ,  0 ,1)
    return data

print (q01_load_data_and_add_column_names(path).head())
