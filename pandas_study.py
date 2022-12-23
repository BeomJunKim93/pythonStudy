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

excel1 = read_data("C:/Users/user/Dropbox/Hongeun119/data/%s" % file_list[5])

df_test1 = pd.DataFrame(excel1)
print(df_test1)
