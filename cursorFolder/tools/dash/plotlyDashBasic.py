import numpy as numpy
import polars as pl
import pandas as pd 
import redis 
import json 
import pickle
import os
import glob
import time


r = redis.Redis(host='localhost', port=6379, db=0)

path = "C:\\Anupam\\GIT\\base\\cursorFolder\\tools\\files"

allFiles = os.listdir(path)
allDF = {}
# print(allFiles)


for file in allFiles:
    df = pl.read_csv(os.path.join(path, file))
    df = df.with_columns(pl.col('Date').str.to_date('%m/%d/%Y'))
    allDates = df['Date'].unique()
    
allDates = allDates.sort(descending=False)

# print(allDates)

for date in allDates:
    print(date)
    redis_value = []
    for file in allFiles:
        df = pl.read_csv(os.path.join(path, file))
        df = df.with_columns(pl.col('Date').str.to_date('%m/%d/%Y'))
        df = df.filter(pl.col('Date') == date)
        print(file)