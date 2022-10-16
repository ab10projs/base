import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv("iris_dataset.csv", sep=',')
plt.close('all') # canvas cleaned
fig= plt.figure(1, figsize=(10,10))
ax1 = plt.subplot2grid((3,3),(0,0))
ax2 = plt.subplot2grid((3,3),(0,1), colspan=2)
ax3 = plt.subplot2grid((3,3),(1,0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3,3),(1,2), rowspan=2)
ax1.hist(iris['petal_width'])
ax2.scatter(iris['petal_length'],iris['petal_width'], s=50*iris['petal_length']*iris['petal_width'],
            alpha=.26, c= iris['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2}))
ax3.scatter(iris['petal_length'],iris['petal_width'], c= iris['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2}))
ax4.violinplot(iris['petal_length'])
plt.suptitle("Fig 1: Grid Plotting Demo", fontsize =20)
plt.tight_layout(pad=5, w_pad=1, h_pad=1)
plt.figure(2, figsize=(12,5))
names= ['gp_a','gp_b','gp_c','gp_d','gp_e','gp_f']
values = [1,2,3,4,5,6]
plt.subplot(131)
plt.bar(names, values, color='orange')
plt.subplot(132)
plt.scatter(names, values, color='orange')
plt.subplot(133)
plt.plot(names, values, color='orange')
plt.suptitle("Fig 2: Row Plotting Demo", fontsize =20)
plt.tight_layout(pad=5, w_pad=1, h_pad=1)
plt.show()