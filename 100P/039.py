#coding:utf-8
#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。


lis=[1,10,100,1000,10000,100000]
n=int(input('insert a number: '))
lis.append(n)
for i in range(len(lis)-1):
    if lis[i]>=n:
        for j in range(i,len(lis)):
            lis[j],lis[-1]=lis[-1],lis[j]
        break
print(lis)