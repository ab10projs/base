# from ctypes import *
# c_file_path = "C:/anupam/minGWPrograms/ClassLibrary1.dll"
# c_func = CDLL(c_file_path)
# print(c_func)
# print("enter 2 numbers")
# a = 1
# b = 9
# result = c_func.addTwoNumbersMethod(a,b)
#
# print(result)

import  clr
clr.AddReference("C:/anupam/minGWPrograms/ClassLibrary1")
from ClassLibrary1 import AddNumbersClass
obj = AddNumbersClass()
print(obj.addTwoNumbersMethod(1,900))