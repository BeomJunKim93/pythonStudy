import pandas as pd
import numpy as np
import pyexcel

def read_data(dir):
    f = open(dir, 'r')
    data = f.readlines()
    f.close()
    return data

data = read_data("./data/2022-09-22 14시 25분 37초.csv")
data2 = read_data("./data/2022-09-24 16시 56분 19초.csv")

res = data + data2[1:]
print(res)

f = open("./새파일2.csv", 'w')
f.writelines(res)
f.close()

c = 6
d = 8
print(c+d)