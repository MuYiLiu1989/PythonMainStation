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
        while True:
            if x not in primes:
                y = random.randint(2,x-1)
                while True:
                    if x%y == 0:
                        z = x//y
                        b = int(input(str(x)+' / '+str(y)+' = '))
                        break
                    else:
                        y = random.randint(2,x-1)
                break
            else:
                x=random.randint(1,100)
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