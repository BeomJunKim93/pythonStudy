# import pandas as pd
# import numpy as np
# import pyexcel
# "D:/Dropbox/Dropbox/Hongeun119/data/파일명.xls"

# def read_data(dir):
#     f = open(dir, 'r')
#     data = f.readlines()
#     f.close()
#     return data
#
# data = read_data("./data/2022-09-22 14시 25분 37초.csv")
# data2 = read_data("./data/2022-09-24 16시 56분 19초.csv")
# #
# # res = data + data2[1:]
# # print(res)
#
# f = open("./새파일2.csv", 'w')
# f.writelines(res)
# f.close()
#
# a = 4
# b = 6
'''
print(a+b)
'''

"""
a + b
"""

number = 3
day = 'three'
a = "I eat %d apples in %s days." % (number, day)
print(a)


import os

file_list = os.listdir('D:/Dropbox/Dropbox/Hongeun119/data')
print(file_list)

def read_data(dir):
    f = open(dir, 'r')
    data = f.readlines()
    f.close()
    return data

data = read_data("D:/Dropbox/Dropbox/Hongeun119/data/%s" % file_list[5])
data2 = read_data("D:/Dropbox/Dropbox/Hongeun119/data/%s" % file_list[6])

res = data + data2[1:]
print(res)

f = open("D:/Dropbox/Dropbox/Hongeun119/data/취합1.xls", 'w')
f.writelines(res)
f.close()