import pandas as pd
import numpy as np
import os # memo
import pyexcel
import win32com.client as win32

# file_dir = './test_data.csv'
#S
#
#

# data = pd.read_csv(file_dir, encoding='utf-8 sig')
# data_arr = data['etcPurps'].values.tolist()
#
# a = data['etcPurps']
# b = a.values
# c = b.tolist()
#
#
# print(data_arr)
# temp_list = []
# for i in data_arr:
#     a = i.split('(')
#     temp_list.append(a[0].replace(' ',''))
#
# data['etcPurps'] = temp_list
# print(data)

# 해당 폴더 내의 파일 목록을 불러옴

base_dir = 'C:/Users/user/PycharmProjects/start1214/'
file_list = os.listdir(base_dir+'홍은data')

print(file_list)

source_dir_win = f'{os.getcwd()}\\홍은data\\'

for file in file_list:
    print(file)
    # data = pd.read_excel(base_dir + '/' + file, engine='xlrd')
    # pyexcel.save_book_as(file_name=base_dir + '/' + file, dest_file_name='./data/' + file.split('.xls')[0]+'.xlsx')

    file_dir = ''
    fdir = f'{source_dir_win}{file}'
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    str= base_dir + '홍은data/' + file
    print(str)
    wb = excel.Workbooks.Open(fdir)
    wb.SaveAs(fdir, FileFormat=51)
    wb.Close()
    excel.Application.Quit()