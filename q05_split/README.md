# Split

Now that you have imported the data, let's split data into target or dependent variable and feature or independent variables. We can use these variables later on to fit a model.

## Write a function `q05_split` that:
- Makes use of the previously created dataframe from q03_encode_features.
- Uses `train_test_split` function to split to X_train, X_test, y_train, y_test

Note: In practice, we denote dependent variables with capital X and target variable with small y.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable | pd.DataFrame | compulsory |  dataframe to be loaded |
| test_size | float | compulsory | 0.3 | split % of test |
| random_state | int | compulsory | 0 | fixing the randomness of the split |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X_train | DataFrame | Dataframe containing feature variables |
| X_test | DataFrame | Dataframe containing feature variables |
| y_train | Series/DataFrame | Target Variable |
| y_test | Series/DataFrame | Target Variable | 