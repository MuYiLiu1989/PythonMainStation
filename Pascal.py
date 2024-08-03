# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:17:54 2024

@author: MuYiAnima
"""

n=int(input("請輸入巴斯卡三角形階層數："))
Pascal = []
rowold = []
for i in range(n):
    if i == 0:
        Pascal.append(1)
    elif i == 1:
        Pascal.append([1,1])
        rowold = [1,1]
    else:
        rownew = []
        rownew.append(1)
        for j in range(len(rowold)-1):
            x = rowold[j]+rowold[j+1]
            rownew.append(x)
        rownew.append(1)
        Pascal.append(rownew)
        rowold = rownew

maxrow = [str(a) for a in Pascal[-1]]
maxstr = ' '.join(maxrow)
length = len(maxstr)
for k in Pascal:
    if k == 1:
        print("{:^{}}".format(k,length).rstrip())
    else:
        strrow = [str(b) for b in k]
        strow = ' '.join(strrow)
        print("{:^{}}".format(strow,length).rstrip())