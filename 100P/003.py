#coding:utf-8
#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# Worst scenario
n=0
while (n+1)**2-n*n<=168:
    n+=1

for i in range((n+1)**2):
    if i**0.5%1==0 and (i+168)**0.5%1==0:
        print(i-100)
