# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv(r"E:\\MachineLearning\\Machine LearningDatasets\DataPreprocessing\Section1\\Python\\Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[:, 1:3]) # does not include the last column
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)