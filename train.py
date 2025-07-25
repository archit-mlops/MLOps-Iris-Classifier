import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

data = pd.read_csv('data/iris.csv')
train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)

X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
y_train = train.species
X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
y_test = test.species

mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
mod_dt.fit(X_train,y_train)
joblib.dump(mod_dt, 'artifacts/model.joblib')