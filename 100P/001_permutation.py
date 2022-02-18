#coding:utf-8
#题目：有四个数字：1、2、3、4，能组成多少个 互不相同 且 无重复数字 的 三位数？各是多少？

count = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (b!=c) and (c!=a):
                print(a,b,c)
                count += 1

print(count)


# Alternative approach
import itertools
count2 = 0
a = [1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    count2 += 1

print(count2)