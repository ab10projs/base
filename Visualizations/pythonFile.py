import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",50)
pd.set_option("display.width", 500)
df = pd.read_csv("iris_dataset.csv")
print(df.head())

s_sepal_length = df['sepal_length'].squeeze()
s_sepal_width =df['sepal_width'].squeeze()
s_petal_length = df['petal_length'].squeeze()
s_petal_width = df['petal_width'].squeeze()
s_species = df['species'].squeeze()

fig, ax = plt.subplots(2,2)
fig.suptitle("Plot Details")

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

ax[0,0].plot(x,y)
ax[0,0].set_title('Axis [0,0] Sine', color ='indigo')
ax[0,0].set_xticklabels(["","one", "two", "three", "four"], fontsize=10, color='blue')
ax[0,1].scatter(s_sepal_length, s_sepal_width, c= s_species.map({'setosa': 0, 'versicolor': 1, 'virginica': 2}))
ax[0,1].set_title("Axis[0,1] Sepats", color = 'red')
ax[1,0].scatter(s_petal_length, s_petal_width, c= s_species.map({'setosa': 0, 'versicolor': 1, 'virginica': 2}))
ax[1,0].set_title("Axis[0,1] Petals", color = 'brown')

import pandas as pd
import numpy as np
import random
lst =[]
randomNumbers= 100
for i in range(randomNumbers):
    lst.append(np.random.randint(0,randomNumbers))
print(lst)
grp_exp = np.array(lst)
print(np.array(lst))
nbins = 21
n, bins, patches = ax[1,1].hist(grp_exp,bins=nbins, edgecolor='black', linewidth= .5)

ax[1,1].set_title("Axis[1,1] Random", color = 'blue')

fig.tight_layout()
plt.show()
