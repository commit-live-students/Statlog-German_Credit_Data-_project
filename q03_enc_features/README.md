# Encoding Features

Before we can model and predict, we need to encode all the categorical features

## Write a function `q03_encode_features` that :

- Makes use of the previously created dataframe from q01_load_data.
- Label encodes all categorical features(using sklearn Label Encoder)

### Parmeters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable | pd.DataFrame | compulsory |  dataframe to be loaded |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Dataframe | Dataframe with above operations inculcated |
