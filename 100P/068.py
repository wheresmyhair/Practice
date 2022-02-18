#coding:utf-8
#题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

def shift(lst,m):
    cache = lst[-m:]
    cache.extend(lst)
    return cache[:len(lst)]

lst = [1,3,4,6,7,8,9]

shift(lst,3)

# Alternative approach
from collections import *
li=[1,2,3,4,5,6,7,8,9]
deq=deque(li,maxlen=len(li))
print(li)
deq.rotate(int(input('rotate:')))
print(list(deq))