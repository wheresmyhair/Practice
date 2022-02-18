#coding:utf-8
#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def isGood(x):
    cache_lst = []
    for i in range(1,x):
        if x%i==0:
            cache_lst.append(i)
    return sum(cache_lst)==x

lst = []

for i in range(1,1000):
    if isGood(i):
        lst.append(i)

print(lst)