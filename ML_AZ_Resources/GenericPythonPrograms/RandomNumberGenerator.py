import pandas as pd
import numpy as np
import re
r = np.random.randint(0,10,10) # Random 10 integers between 0 and 100
#r = np.random.random_sample (10) # random 10 floats between 0 and 1
#r = np.random.random(30) *100   #This gives 30 random floats
#r = np.random.uniform(0,10,(10))  #This gives random floats between 2 numbers
f= open('f.csv', 'w')
for i in r:
    f.write(str(i) )
    f.write(",\n")
print(r)