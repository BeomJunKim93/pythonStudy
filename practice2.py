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
#
# number = 3
# day = 'three'
# a = "I eat %d apples in %s days." % (number, day)
# print(a)
#
#
import os

file_list = os.listdir('D:/Dropbox/Dropbox/Hongeun119/data')
print(file_list)

# find = file_list.index('취합1.xls')
# print(find)
#
# find2 = file_list[2]
# print(find2)


def read_data(dir):
    f = open(dir, 'r')
    data = f.readlines()
    f.close()
    return data

excel1 = read_data("D:/Dropbox/Dropbox/Hongeun119/data/%s" % file_list[5])
excel2 = read_data("D:/Dropbox/Dropbox/Hongeun119/data/%s" % file_list[6])

print(excel1)
print(excel2)
#
# res = data + data2[1:]
# print(res)
#
# excel1.append(excel2[1:])
# print(excel1)
#
# excel3 = excel1.insert(0,excel2[1:])
# print(excel3) 이건 안되네

#
# f = open("D:/Dropbox/Dropbox/Hongeun119/data/취합3.xls", 'w')
# f.writelines(excel1)
# f.close()


import pandas as pd
import numpy as np
import pyexcel
import os
# "D:/Dropbox/Dropbox/Hongeun119/data/파일명.xls", 노트북 주소
# C:/Users/user/Dropbox/Hongeun119/data, 연구실 컴터 주소

# obj = pd.Series([4,7,-5,3])
# print(obj)
# '''Series 정의하기'''
#
# print(obj.values)
# '''Series의 값만 확인'''
#
# print(obj.index)
# '''인덱스만 확인'''

file_list = os.listdir('C:/Users/user/Dropbox/Hongeun119/data')
# df_file_list = pd.DataFrame(file_list)
# print(df_file_list)

def read_data(dir):
    f = open(dir, 'r')
    data = f.readlines()
    f.close()
    return data

excel1 = read_data("C:/Users/user/Dropbox/Hongeun119/data/%s" % file_list[5])
excel2 = read_data("C:/Users/user/Dropbox/Hongeun119/data/%s" % file_list[6])

df_test1 = pd.DataFrame(excel1)
print(df_test1)
df_test2 = pd.DataFrame(excel2)
print(df_test2)

res = excel1 + excel2[1:]
df_res = pd.DataFrame(res)
print(df_res)

# excel1.append(excel2[1:])
# print(excel1)