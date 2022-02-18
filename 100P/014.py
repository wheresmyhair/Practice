#coding:utf-8
#题目：将一个整数分解质因数。

import sys

target=int(input('Integer: '))

if target<0:
    sys.exit('Check input')

print(f'{target}=',end='')

flag=0

if target<=1:
    print(target)
    flag=1

while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print(i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break