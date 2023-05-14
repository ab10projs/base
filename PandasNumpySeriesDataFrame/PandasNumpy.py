import pandas as pd
print("series")

lis = ['l1','l2','l3','l4']
print(lis)
l1 = pd.Series(lis)
print(l1)

dict1 = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5',}
print(pd.Series(dict1))