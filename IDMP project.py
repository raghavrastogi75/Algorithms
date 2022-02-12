# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:36:51 2021

@author: ragha
"""

import pandas as pd

df = pd.read_csv (r'data1.csv')
#print (df)

# Data Cleaning

df = df[df.familysize <= 25]

df = df[(df.VCL9 == 0) | (df.VCL6 == 0) | (df.VCL12 == 0)]

df = df[df.age <= 100]

df = df.drop('major', 1)

df["Total_time"] = df.apply(lambda row: (row.Q1E + row.Q2E +
                                         row.Q3E + row.Q4E + row.Q5E + 
                                         row.Q6E + row.Q7E + row.Q8E +row.Q9E + 
                                         row.Q10E + row.Q11E + row.Q12E + row.Q13E +                                         
                                         row.Q14E + row.Q15E + row.Q16E + row.Q17E + 
                                         row.Q18E + row.Q19E + row.Q20E + row.Q21E +
                                         row.Q22E + row.Q23E + row.Q24E + row.Q25E +
                                         row.Q26E + row.Q27E + row.Q28E + row.Q29E + 
                                         row.Q30E + row.Q31E + row.Q32E + row.Q33E +
                                         row.Q34E + row.Q35E + row.Q36E + row.Q37E +
                                         row.Q38E + row.Q39E + row.Q40E + row.Q41E +
                                         row.Q42E)/1000, axis=1)

df = df[(df.Total_time <= 3600) & (df.Total_time >= 100) ]



l = ["Q1A","Q2A","Q3A","Q4A","Q5A","Q6A","Q7A","Q8A","Q9A","Q10A","Q11A","Q12A","Q13A","Q14A","Q15A","Q16A","Q17A","Q18A","Q19A","Q20A" ,"Q21A","Q22A","Q23A","Q24A","Q25A" ,"Q26A","Q27A","Q28A","Q29A","Q30A","Q31A","Q32A","Q33A","Q34A","Q35A","Q36A","Q37A","Q38A","Q39A","Q40A","Q41A","Q42A"]

for i in l:
    
    df.loc[df[i] == 1, i] = 0
    df.loc[df[i] == 2, i] = 2
    df.loc[df[i] == 3, i] = 4
    df.loc[df[i] == 4, i] = 6
    
df["Depression score"] = df.apply(lambda row: row.Q3A + row.Q5A +  row.Q10A + row.Q13A + row.Q16A + row.Q17A + row.Q21A +row.Q24A +   row.Q26A +  row.Q31A + row.Q34A + row.Q37A + row.Q38A + row.Q42A , axis=1)
df["Anxiety score"] = df.apply(lambda row: row.Q2A + row.Q4A +  row.Q7A + row.Q9A + row.Q15A + row.Q19A + row.Q20A + row.Q23A +row.Q25A + row.Q28A +  row.Q30A + row.Q36A + row.Q40A + row.Q41A , axis=1)
df["Stress score"] = df.apply(lambda row: row.Q1A + row.Q6A +  row.Q8A + row.Q11A + row.Q12A + row.Q14A + row.Q18A + row.Q22A +row.Q27A + row.Q29A +  row.Q32A + row.Q33A + row.Q35A + row.Q39A , axis=1)

print(df)