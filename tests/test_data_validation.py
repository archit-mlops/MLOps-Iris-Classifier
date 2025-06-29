import pandas as pd

def test_dataset_not_empty():
    df = pd.read_csv('data/iris.csv')
    assert not df.empty, 'Dataset is empty'
    
def test_required_columns_exist():
    df = pd.read_csv('data/iris.csv')
    expected_columns = {"sepal_length", "sepal_width", "petal_length", "petal_width", "species"}
    assert expected_columns.issubset(set(df.columns)), "Missing one or more required columns"
    
def test_no_null_values():
    df = pd.reaD_csv('data/iris.csv')
    assert df.isnull().sum().sum() == 0, 'Dataset contains null values'