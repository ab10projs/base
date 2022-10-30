import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Button

class Cluster(object):
    ind= 0
    def next(self, event):
        self.ind +=1
        i = self.ind % len(species)
        index= iris['species'] == species[i]
        axs.clear()
        axs.scatter(x[index], y[index], s= 50, marker ='o')
        axs.set_title(species[i], size=25, color= 'r')
        plt.draw()

    def prev(selfself, event):
        self.ind -= 1
        i = self.ind % len(species)
        index = iris['species'] == species[i]
        axs.clear()
        axs.scatter(x[index], y[index], s=50, marker='o')
        axs.set_title(species[i], size=25, color='r')
        plt.draw()
cluster = Cluster()

iris = pd.read_csv("iris_dataset.csv", delimiter= ',')
species = ['setosa','versicolor','virginica']
x,y = iris['petal_length'], iris['petal_width']
index = iris['species']==species[cluster.ind]

fig, axs = plt.subplots()
axs.scatter(x[index], y[index], s=50, marker= 'o')
axs.set_title(species[cluster.ind], color = 'r', size =25)

axprev= plt.axes([.7,.005, 0.1,.005])
axnext = plt.axes([.81, .005,.1, .05])

bnext = Button(axnext, "Next")
bprev = Button(axprev, "Prev")

bnext.on_clicked(cluster.next)
bprev.on_clicked(cluster.prev)

plt.show()

