import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('ggplot')

#---- 1 ---- Start
# x = np.arange(0,10,.2)
# y = np.sin(x)
# z = np.cos(x)
# print(y)
# print(z)
# print(plt.style.available)
# plt.style.use('ggplot')
# # plt.plot([1,2,3,4],[11,22,33,44])
# # plt.show()
# # plt.scatter([1,2,3,4],[11,22,33,44])
# # plt.show()
# plt.scatter(x,y)
# plt.xlabel ('X val')
# plt.ylabel('Y val')
# plt.title ('Sine Chart')
# plt.show()
#---- 1 ---- End

#---- 2 ---- Start
# df_gold= pd.read_csv("E:/Python_Projects/CorePython/UdemyVizData/Data Visualization with Python/Data/GoldPrice.csv", index_col= 'date')
# print(df_gold.head())
# plt.scatter(df_gold.index, df_gold['value'])
# plt.show()
#---- 2 ---- End

#---- 3 ---- Start
# x = np.arange(0,10,.2)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x,y, x,z)
# #or
# plt.plot(x,y)
# plt.plot(x,z)
# plt.show()
#---- 3 ---- End

#---- 4 ---- Start
# x = np.arange(0,10,.2)
# y = np.sin(x)
# z = np.cos(x)
# plt.subplot(1,2,1)
# plt.scatter(x,y, color='red')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("first Chart")
# plt.subplot(1,2,2)
# plt.scatter(x,z,color='blue')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Second Chart")
# plt.show()

#---- 4 ---- End
#---- 5 ---- Start
x = np.arange(0,10,.2)
y = np.sin(x)
z = np.cos(x)


plt.subplot(2,1,1)
plt.plot(x,y)
plt.subplot(2,1,2)
plt.plot(x,z)
plt.show()

#---- 5 ---- End



