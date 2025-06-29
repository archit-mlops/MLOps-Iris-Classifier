import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def test_model_accuracy_above_threshold():
    model = joblib.load('artifacts/model.joblib')
    df = pd.read_csv('data/iris.csv')
    X = df.drop('species', axis=1)
    y = df['species']

    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)

    assert acc > 0.90, f'Accuracy {acc:.2f} below threshold'