import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
print(dataset)
x= dataset.iloc[:,:-1].values
y= dataset.iloc[:,-1].values
print(y)

from sklearn.impute import SimpleImputer  #import module SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean') # create an instance and tell to use mean
imputer.fit(x[:,1:3]) # fit the instance on data
x[:,1:3] = imputer.transform(x[:,1:3]) # transform and replace the data
#print(x)

from sklearn.compose import ColumnTransformer #import compose module and ColumnTransform class
from sklearn.preprocessing import OneHotEncoder #import preprocessing module and its class called OneHotEncoder
#below , an instance called ct is created,
# ColumnTransform takes 3 paramentes
# [0] means the transformation is to be applied on 0th column.
# In single step the fit and transform is called and an array is created and is passed to x
# remainder means that the other columns are to be kept as it is.
# what type of trasformation? --> éncoding', wathat type of encoding? --> OneHoteEncoder... All these are mented in a touple
# if remainder ='passthrough'is omited , then the Age and Salary columns will be dropped
# the model expects the output as numpy array, so explicit conversion is done.
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(), [0])], remainder='passthrough')
x = np.array ( ct.fit_transform(x))

# if there are columns with only two values(Yes/No), then we use label encoder
# for LabelEncoder, only vector(not 2d df) is passed as input, so y , which is a vector of Yes and No is passed and it is converted to 0,1
from sklearn.preprocessing import LabelEncoder
lbl_encdr = LabelEncoder()
y = np.array(lbl_encdr.fit_transform(y))
print(y)
