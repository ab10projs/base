
import polars as pl
import pandas as pd
import redis
import os
import json
import time

##
'''
- This section will read a key (symbol) from redis and store in rolling window
of 30 latest values. 
- all basic stats will be calculated and displayed on the dashboard.
using dash framework.

'''
##

r = redis.Redis(host='localhost', port=6379, db=0)
# print(json.loads( r.get( str(keys()))))
print( r.keys())
for key in r.keys():
    print(key.decode('utf-8'))
    print(json.loads( r.get( str(key.decode('utf-8')))))







