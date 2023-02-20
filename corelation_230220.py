import openpyxl
import pandas as pd
import openpyxl as oxl
import numpy as np
import os
import matplotlib.pyplot as plt

#
# df = pd.read_excel('./kdw_set_result.xlsx')
# print(df.corr(method='pearson', min_periods=1))
#
# plt.scatter(df['base'], df['heat'])
# plt.show()

df = pd.read_excel('./최종처리결과_V1.xlsx')

df = df[(df['type_before'] != 'ERROR_NOFIT') & (df['type_before'] != 'ERROR_trial_exceeded') & (pd.notna(df['type_before']))]
df = df[(df['type_after'] != 'ERROR_NOFIT') & (df['type_after'] != 'ERROR_trial_exceeded') & (pd.notna(df['type_after']))]

print(df)

preproc_arr = ['sum_before', 'sum_after', 'hsl_before',
       'csl_before', 'hcp_before', 'ccp_before', 'heat_before', 'cool_before',
       'base_before', 'hsl_after', 'csl_after', 'hcp_after',
       'ccp_after', 'heat_after', 'cool_after', 'base_after']

for col in preproc_arr:
    df[col] = df[col]/df['연면적(m2)']
    df[col] = df[col].astype('float32')
    
df['csl_gap'] = df['csl_after'] - df['csl_before']
df['hsl_gap'] = df['hsl_after'] - df['hsl_before']
df['heat_gap'] = df['heat_after'] - df['heat_before']
df['cool_gap'] = df['cool_after'] - df['cool_before']
df['ccp_gap'] = df['ccp_after'] - df['ccp_before']
df['hcp_gap'] = df['hcp_after'] - df['hcp_before']
df['base_gap'] = df['base_after'] - df['base_before']

res_proc_arr = ['csl_gap', 'hsl_gap', 'heat_gap', 'cool_gap', 'ccp_gap', 'hcp_gap', 'base_gap']

use_cols = ['연면적(m2)', '총공사금액(원)', '창호금액(원)', '보일러금액(원)', '단열제금액(원)', '중문금액(원)', '조명(LED)금액(원)'] + res_proc_arr
df = df[use_cols]

print(df)
print(df.info())
df.to_excel('./processed_data.xlsx')