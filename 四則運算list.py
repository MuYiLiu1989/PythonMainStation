# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:07:26 2024

@author: MuYiAnima
"""

import random

primes = []
for i in range(2,101):
    for x in range(2,i):
        if i%x == 0:
            break
    else:
        primes.append(i)

full = []    
for i in range(4,101):
    full.append(i)
#print(full)
not_primes = []
for i in full:
    if i not in primes:
        not_primes.append(i)
#print(not_primes)
while True:
    a = int(input("請輸入1=>+,2=>-,3=>*,4=>/,5=>quit:"))
    x=random.randint(1,100)
    y=random.randint(1,100)
    
    if a == 1:
        z = x + y
        b = int(input(str(x)+' + '+str(y)+' = '))
        
    elif a == 2:
        z = x - y
        b = int(input(str(x)+' - '+str(y)+' = '))
        
    elif a == 3:
        z = x * y
        b = int(input(str(x)+' * '+str(y)+' = '))
    elif a == 4:
        ind1 = random.randint(0,len(not_primes)-1)
        x = not_primes[ind1]
        insu = []
        for i in range(2,x):
            if x%i==0:
                insu.append(i)
        #print(insu)
        ind2 = random.randint(0,len(insu)-1)
        y = insu[ind2]
        z = x//y
        b = int(input(str(x)+' / '+str(y)+' = '))
    elif a == 5:
        break
    else:
        print("輸入錯誤，再輸一次")
        continue
        
    if b == z:
        print("答對了")
    else:
        print("答錯了，答案是",z)
        
print("程式結束")