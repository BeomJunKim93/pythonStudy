import openpyxl
import pandas as pd
import openpyxl as oxl
import numpy as np
import os
# try1
# def read_data(dir):
#     f = open(dir, 'r')
#     data = f.readlines()
#     f.close()
#     return data
#
# file_main = read_data("./5.북부여성발전센터.xlsx")
# try2
# wb = load_workbook('./pandas_study/5.북부여성발전센터.xlsx')
# ws = wb.active
#
# ws.unmerge_cells('A1:H1')
#
# df2 = pd.DataFrame(ws.unmerge_cells)
# print(df2)

# 엑셀 파일 불러오기
file_main = './pandas_study/5.북부여성발전센터.xlsx'
# 워크북 (파일 자체) 불러오기
wb = openpyxl.load_workbook(file_main)
# 워크시트 불러오기
ws = wb['기본정보']

# 열 (Column) 값 확인하기
for cell in ws['D']:
    print(cell.value)



