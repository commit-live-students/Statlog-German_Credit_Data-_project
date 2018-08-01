# Build your own model

Now you are well aware of the different Models and hyperparameter techniques.
You are free to use any model you want to apply which has been taught to you.

## Write a function `q07_randomsearch_predict` that:

- Makes use of the return variables of q05_feature_preprocessing
- Models the train according to your data and returns the `roc_auc_score`

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| X_train | DataFrame | compulsory |Dataframe containing feature variables(train) |
| X_test | DataFrame |compulsory | Dataframe containing feature variables(test) |
| y_train | Series/DataFrame |compulsory | Target Variable(train)|
| y_test | Series/DataFrame |compulsory | Target Variable(test) |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| roc_auc_score | float | ROC AUC score |