from sklearn.model_selection import train_test_split
<<<<<<< HEAD
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'


=======
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features, q01_load_data_and_add_column_names
path = './data/GermanData.csv'
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
    
>>>>>>> 909c0ea60336b196926e226307816947a629d970
