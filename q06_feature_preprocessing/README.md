# Feature Preprocessing

Good job so far

Now let's look at most important features.Since you have learned the technique of selecting `k best features`.

## Write a function `q06_feature_preprocessing` that:

- Makes use of the return variables of q05_split
- Scales both X_train and X_test(using MinMaxScaler)
- Oversamples the data(using Smote)(Intuition behind it is the imbalanced target variable distribution)
- Selects kbest features(k=8, using SelectKBest)
- Returns the four transformed variables after the above operations

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| X_train | DataFrame | compulsory ||Dataframe containing feature variables(train) |
| X_test | DataFrame |compulsory || Dataframe containing feature variables(test) |
| y_train | Series/DataFrame |compulsory || Target Variable(train)|
| y_test | Series/DataFrame |compulsory || Target Variable(test) |
| random_state | int |compulsory | 0 | fixing the randomness in the SMOTE function |
| k | int |compulsory | 8 | select the Kbest features

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X_train | DataFrame | Dataframe with above operations inculcated |
| X_test | DataFrame | Dataframe with above operations inculcated |
| y_train | Series/DataFrame | Target Variable with above operations inculcated |
| y_test | Series/DataFrame | Target with above operations inculcated |

