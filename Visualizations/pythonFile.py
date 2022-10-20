import matplotlib.pyplot as plt
import pandas as pd

wine_qty = pd.read_csv("winequality.csv", delimiter=";")
iris = pd.read_csv("iris_dataset.csv", delimiter=',')
iris_mean = iris.mean()
iris_std = iris.std()
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
axs[0, 0].hist(wine_qty['alcohol'])
axs[0, 0].set_title("Title Alcohol Frequency")
axs[0, 0].set_xlabel('Alcohol Bin')
axs[0, 0].set_ylabel("Frequency")
axs[0, 1].plot(iris['sepal_length'])
axs[0, 1].set_title("Sepal L Frequency")
axs[0, 1].set_xlabel('sepal_length')
axs[0, 1].set_ylabel("sepal frequency")
axs[1, 0].scatter(iris['petal_length'], iris['petal_width'],
                  c=iris['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2}))
axs[1, 0].set(title='Scatter', xlabel='Petal Len', ylabel='Petal Wd')
axs[1, 1].bar(['sepal_l', 'sepal_w', 'petal_l', 'petal_w'], iris_mean, yerr=iris_std)
axs[1, 1].set(title='Bar', xlabel='category', ylabel='Category Mean')
plt.suptitle("Subplots")
plt.tight_layout(pad=3, w_pad=1, h_pad=1)
plt.show()
