import pandas as pd
import numpy as np
import pyexcel

#
# file_dir = 'C:\Users\user\PycharmProjects\pythonStudy\2022-09-22 14시 25분 37초.csv'
#
# data = pd.read_csv(file_dir, encoding='utf-8 sig')

csv_test1 = pd.read_csv('./data/2022-09-22 14시 25분 37초.csv', encoding='ANSI')
# print(csv_test1)

csv_test2 = pd.read_csv('./data/2022-09-24 16시 56분 19초.csv', encoding='ANSI')
# print(csv_test2)
#
# # merge files
# dataFrame = pd.concat(
#    map(pd.read_csv, [csv_test1, csv_test2]))
# print(dataFrame)

df_test1 = pd.DataFrame(csv_test1)
print(df_test1)
df_test2 = pd.DataFrame(csv_test2)
print(df_test2)

concat_test = pd.concat([df_test1, df_test2])
print(concat_test)

concat_test.to_csv("result1.csv")

