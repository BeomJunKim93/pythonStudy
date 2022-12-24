# -*- coding: utf-8 -*-
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

# try 3
# print(wb.sheetnames)

# # 워크시트 불러오기
# ws = wb['기본정보']
#
# # 열 (Column) 값 확인하기
# for cell in ws['A']:
#     print(cell.value)
# print(len(ws['A']))

# 워크시트 생성하기
wb = openpyxl.Workbook()
ws = wb.active

column_value = ['파일명','기관구분코드','책임자 E-mail','부서명','성명','연락처','E-mail','건물명','지번주소','도로명주소','준공년도','건축물층수','건축물구조','건축물방위','기준층 천장고','연면적','기준층 층고','지하주차장','PC수','근무인원','IP 발급수','방문인원','일 근무시간','근무마감 시간','수영장유무','수영장면적','증 개축여부','증.개축 변동면적','증․개축 년도','증.개축 변동층수','증.개축 용도변경결과','전기 계량기 번호','가스 계량기 번호']
print(len(column_value))

for i in range(len(column_value)):
    ws.cell(row = 1, column = i).value = column_value[i]

print(ws)

# ws[column[0]] = column_value[0]
# ws[column[1]] = column_value[1]
# ws[column[2]] = column_value[2]
# for i in range(len(column)):
#     ws[column[i]] = column_value[i]
#     print(ws[column[i]].value)
# wb.save('test_write.xlsx')
#
#
# # 엑셀 파일 불러오기
# file_main = './pandas_study/5.북부여성발전센터.xlsx'
# # 워크북 (파일 자체) 불러오기
# wb = openpyxl.load_workbook(file_main)
# ws = wb['기본정보']
# sheet1 = ws.cell(row=1, column=1).value
# print(sheet1)

