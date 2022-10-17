import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",50)
pd.set_option("display.width", 500)
df = pd.read_csv("iris_dataset.csv")

#print(df[df['species']=='setosa']['sepal_length'].sum())

allSpecies=[]
allSpeciesSepal_length=[]
for x in (df['species'].unique()):
    allSpecies.append(x)

for x in allSpecies:
    allSpeciesSepal_length.append(df[df['species']=='{}'.format(x)]['sepal_length'].sum())


print(allSpecies, allSpeciesSepal_length)
totalSepalLength = np.sum(allSpeciesSepal_length)
print(totalSepalLength)
plt.bar(allSpecies,allSpeciesSepal_length)
plt.pie(allSpeciesSepal_length, labels=allSpecies, autopct='%1.1f%%', shadow=True,startangle=90 )
plt.show()