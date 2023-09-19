import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset.
# .values converts the dataframe into list of lists
dataset = pd.read_csv("data\\Data.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
print(X)
print("--")
from sklearn.impute import SimpleImputer  # SimpleImputer imported
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:,1:3])  #X is a list, converted by using .values from dataframe. 1:3 means leave 0th and 3rd column as only numeric columns should be considered
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)
print("0000")


from sklearn.compose import ColumnTransformer
# OneHoteEncoder converts a category into code like [0 1 0] etc.
from sklearn.preprocessing import OneHotEncoder

# here two classes are used... ColumnTransformer and OneHotEncoder
# the 'transformers' argument takes parameters in form of a list
# transformers=[('encoder', OneHotEncoder(),[0])] tells what type of transformation is needed
# the [0] tells that the transformation is to be applied on 0th column
# remainder='passthrough' tells that the other columns should remain as they are and not dropped
# np.array is called to force the output as array
# fit_transform .. here this method does both fit and trasform in one step

ct = ColumnTransformer( transformers=[('encoder', OneHotEncoder(),[0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(Y)
print(Y)




