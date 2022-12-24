import websockets
import asyncio
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
mplstyle.use('fast')

import win32com.client as win32
import os

# 경로 및 파일목록 불러오기 (공통부)
# base_dir = './'
# file_list = os.listdir(base_dir+'data_csv')
# print(file_list)

def replace_str_inarr(arr, a_str, b_str):
    print(arr)
    res = []
    for item in arr:
        res.append(item.replace(a_str, b_str))
    # print(res)
    return res

# res = pd.concat(df_arr)
# res.to_csv('./bind_data/취합결과_V2.csv', encoding='utf-8 sig')
# raise IOError




matplotlib.rc('font', family='NanumGothic') #한글 폰트 적용시

# 그래프 출력
data = pd.read_csv('./bind_data/취합결과_V2.csv', index_col=0)
print('loaded')
# data = data[(data.index.to_series().astype('datetime64[ns]').dt.month == 11)]
# data = data[0:100000]
data.index = pd.to_datetime(data.index)

# forward_data = data[(data.index < '2022-09-30 15:19:40')]
# backward_data = data[(data.index >= '2022-09-30 15:19:40')]
#
# def replace_str_inarr(arr, a_str, b_str):
#     print(arr)
#     res = []
#     for item in arr:
#         res.append(item.replace(a_str, b_str))
#     # print(res)
#     return res
#
# forward_data.columns = replace_str_inarr(forward_data.columns.values.tolist(), '1(구급우)', '1(심신좌)')
# forward_data.columns = replace_str_inarr(forward_data.columns.values.tolist(), '3(심신좌)', '3(구급우)')
#
# backward_data.columns = replace_str_inarr(backward_data.columns.values.tolist(), '1(구급우)', '3(구급우)')
# backward_data.columns = replace_str_inarr(backward_data.columns.values.tolist(), '3(심신좌)', '1(심신좌)')
#
# data = pd.concat([forward_data, backward_data], ignore_index=True)
# data.set_index('Time', drop=True, inplace=True)
# data.index = pd.to_datetime(data.index)


# data = data[['3(구급우)in(℃)', '3(구급우)out(℃)', '3(구급우)in(%)', '3(구급우)out(%)', '3(구급우)(W)', '3(구급우)(kWh)', '2(구급중)in(℃)', '2(구급중)out(℃)', '2(구급중)in(%)', '2(구급중)out(%)', '2(구급중)(W)', '2(구급중)(kWh)', '1(심신좌)in(℃)', '1(심신좌)out(℃)', '1(심신좌)in(%)', '1(심신좌)out(%)', '1(심신좌)(W)', '1(심신좌)(kWh)', '실외기(W)', '실외기(kWh)', '급탕히트펌프(W)', '급탕히트펌프(kWh)', 'BF1-PVT 축열조 inlet 시수(㎥/h)P']]

print(data)

def filter_200(num):
    if num > 200:
        return 0
    else:
        return num
data['실외기(W)'] = data['실외기(W)'].apply(filter_200)
data['급탕히트펌프(W)'] = data['급탕히트펌프(W)'].apply(filter_200)
# res = data[['1(구급우)in(℃)', '1(구급우)out(℃)', '1(구급우)in(%)', '1(구급우)out(%)', '1(구급우)(W)', '1(구급우)(kWh)', '2(구급중)in(℃)', '2(구급중)out(℃)', '2(구급중)in(%)', '2(구급중)out(%)', '2(구급중)(W)', '2(구급중)(kWh)', '3(심신좌)in(℃)', '3(심신좌)out(℃)', '3(심신좌)in(%)', '3(심신좌)out(%)', '3(심신좌)(W)', '3(심신좌)(kWh)', '실외기(W)', '실외기(kWh)', '급탕히트펌프(W)', '급탕히트펌프(kWh)', 'BF1-PVT 축열조 inlet 시수(㎥/h)P']]
# res.to_csv('./data_csv/취합결과_컬럼필터.csv', encoding='utf-8 sig')

# 데이터 처리
data = data.replace(0, np.nan)
# data = data.dropna()

data = data.resample('1T').mean()
print(data)

column_list = ['3(구급우)in(℃)', '3(구급우)out(℃)', '3(구급우)in(%)', '3(구급우)out(%)', '3(구급우)(W)', '3(구급우)(kWh)']
for colname in column_list:
    temp_data = data[[colname]]
    plt.scatter(temp_data.index, temp_data[colname], label=colname, s=1)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), scatterpoints=3, markerscale=5)
# plt.savefig('./binded_total_result_nov_v2.png')
plt.show()

raise IOError



'''
col_arr = data.columns.values.tolist()
unit_arr = ['℃', '%', 'W', 'kWh', '㎥/h']
unit_col_arr = []

for unit in unit_arr:
    temp_arr = []
    for colname in col_arr:
        if '(' + unit + ')' in colname:
            temp_arr.append(colname)
    unit_col_arr.append(temp_arr)

from matplotlib import colors
colorlist = list(colors.ColorConverter.colors.keys())
watt_colorlist = ['red', 'pink', 'salmon']
coeff_arr = [1, 1, 1]
plt.figure(figsize=(14, 9))
i = 0
j = 0
for unit in ['℃', '%', 'W']: # unit_arr:
    temp_data = data[unit_col_arr[unit_arr.index(unit)]]
    # plt.figure(figsize=(12, 9))
    for col in temp_data.columns.values.tolist():
        if col in ['실외기(W)', '급탕히트펌프(W)']:
            pass
        else:
            if unit == 'W':
                plt.scatter(temp_data.index, temp_data[col] * coeff_arr[unit_arr.index(unit)], label=col, s=1, c=watt_colorlist[j])
                j = j + 1
            else:
                plt.scatter(temp_data.index, temp_data[col]*coeff_arr[unit_arr.index(unit)], label=col, s=1, c = colorlist[i])
                i = i + 1
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), scatterpoints=3, markerscale=5)
    # plt.savefig('./binded_total_result_nov_v2.png')
    plt.show()

'''


raise IOError






# # 경로 및 파일목록 불러오기 (공통부)
# base_dir = './'
# file_list = os.listdir(base_dir+'data_csv')
# print(file_list)
#
# # csv파일 취합부
# df_arr = []
# for file in file_list:
#     print(file)
#     temp_data = pd.read_csv(base_dir+'data_csv/'+file, encoding='ANSI')
#     temp_data.set_index('Time', drop=True, inplace=True)
#     df_arr.append(temp_data)
# res = pd.concat(df_arr)
# res.to_csv('./data/취합결과.csv', encoding='utf-8 sig')
# raise IOError

# xls >> xlsx 파일 변환부
'''source_dir_win = f'{os.getcwd()}\\홍은data\\'
for file in file_list:
    print(file)
    file_dir = ''
    fdir = f'{source_dir_win}{file}'
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    str= base_dir + '홍은data/' + file
    wb = excel.Workbooks.Open(fdir)
    # wb.SaveAs(fdir+'x', FileFormat=51)
    filename_str = fdir[0:-3]+'csv'
    wb.SaveAs(filename_str, FileFormat=6)
    wb.Close(SaveChanges=True)
    excel.Application.Quit()
raise IOError'''