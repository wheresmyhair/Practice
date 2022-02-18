#coding:utf-8
#题目：求1+2!+3!+...+20!的和。

from math import factorial


sum = 0
for i in range(1,21):
    sum += factorial(i)
print(sum)


res = 1
for i in range(20,1,-1):
    res = i*res+1
print(res)
