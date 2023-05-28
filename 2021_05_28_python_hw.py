# -*- coding: utf-8 -*-
"""2021_05_28_Python_HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S-25pj_IFaMCTm5tVnskn6QXK4SYHfeU
"""

import pandas as pd
import seaborn as sns
import google.colab as files

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv', sep = ';', encoding='cp1251')
df

"""Задача 1. Найдите, какая область центрального федерального округа имела наибольшую
численность студентов вечерней формы обучения в 2015 году.
"""

df_task_01 = df.iloc[3:20, :]
max_value = df_task_01['Численность студентов заочная форма, человек, 2015'].max()
df_task_01_res = df_task_01[df_task_01['Численность студентов заочная форма, человек, 2015']==max_value]
df_task_01_res = pd.DataFrame(df_task_01_res, columns = ['Субъект РФ', 'Численность студентов заочная форма, человек, 2015'])
df_task_01_res

"""Задача 2. Постройте диаграмму с данными о численности студентов дневной формы
обучения южного федерального округа за 2017 год.
"""

df_task_02 = df.iloc[33:41, :]
plot = sns.barplot(df_task_02, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(labels = df_task_02['Субъект РФ'], rotation = 90)

"""Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019
год по всем регионам, в которых общее количество студентов не превышает 10000 за
данный год
"""

msk_1 = df['Субъект РФ'].str.contains('округ')
df_task_03 = df.drop(df[msk_1].index)
msk_2 = df['Субъект РФ'].str.contains('Федерация')
df_task_03 = df_task_03.drop(df_task_03[msk_2].index)
df_task_03 = df_task_03[df_task_03['Численность студентов заочная форма, человек, 2019'] <= 10000]
plot = sns.barplot(df_task_03, x = 'Субъект РФ', y = 'Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(labels = df_task_03['Субъект РФ'], rotation = 90)