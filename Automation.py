# -*- coding: utf-8 -*-
"""

@author: ASUS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import smtplib

excel_file_1 = 'shift-data.xlsx'

#reading different sheets
df_first_shift = pd.read_excel(excel_file_1, sheet_name='first')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='second') 

print(df_first_shift)

#print(df_second_shift.shape)


# concatiing the two sheets in one
df_all = pd.concat([df_first_shift,df_second_shift])

#groupby shift to fins out mean
pivot = df_all.groupby(['Shift'],as_index=False).mean()
povot = pivot[['Production Run Time (Min)','Products Produced (Units)']]

povot.plot(kind = 'pie',subplots = True)


print(~df_all['Production Run Time (Min)'].isnull())


lst = [['hero','zero'],['one'],['two']]
x = "save_file"

saveFile = open("{}.txt".format(x),'w')
for i in lst:
    saveFile.write(str(i)+'\n')
saveFile.close()
    

'''
email = 'attendance707@gmail.com'
password = 'Hero#707'



pivot =  pivot[['Shift','Production Run Time (Min)','Products Produced (Units)']]
email_dict = { 1: 'shreeshailkandi@gmail.com',
              2: 'shubhamchavan9519@gmail.com'}

Shift = pivot['Shift'].unique()
for i,row in pivot.iterrows():
    for n in Shift:
        if row['Shift'] == n and row['Production Run Time (Min)'] >40:
            subject = 'Attendance'
            body = 'Hello, The attendace for this week is {} which is below our desired level of 50 hrs. Please connect with the HR'.format(row['Production Run Time (Min)'])
            msg =  f"Subject :{subject}\n\n{body}"
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.login(email,password)
            server.sendmail(email,email_dict[n],msg)
    
    
'''