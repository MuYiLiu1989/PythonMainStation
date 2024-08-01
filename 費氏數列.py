# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:24:40 2024

@author: MuYiAnima
"""

n = int(input("請輸入整數："))
Fe = [1,1]
for i in range(2,n+2):
    x = Fe[i-1]+Fe[i-2]
    Fe.append(x)
print(Fe)