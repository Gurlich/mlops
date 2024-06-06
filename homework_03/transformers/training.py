import pandas as pd
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

import mlflow

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_model(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    mlflow.set_tracking_uri("http://magic-mlflow:5000")
    mlflow.set_experiment("mage-experiment")

    
    categorical = ['PULocationID', 'DOLocationID']

    with mlflow.start_run():

        df[categorical] = df[categorical].astype(str)

        train_dicts = df[categorical].to_dict(orient='records')

        dv = DictVectorizer()
        X_train = dv.fit_transform(train_dicts)

        # train model
        target = 'duration'
        y_train = df[target].values

        lr = LinearRegression()
        lr.fit(X_train, y_train)

        print("lr.intercept_")
        print(lr.intercept_)

        mlflow.log_param("intercept", lr.intercept_)
        # mlflow. (lr, artifact_path="models")
        
        # log DictVect
        with open('dv.pkl', "wb") as f_out:
            pickle.dump(dv, f_out)
        mlflow.log_artifact('dv.pkl', artifact_path='DictVect')

        # log model
        mlflow.sklearn.log_model(lr, artifact_path="models")

        print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")

    return lr, dv


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'




