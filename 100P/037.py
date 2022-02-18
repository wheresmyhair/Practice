#coding:utf-8
#题目：对10个数进行排序。

lst = []
for i in range(10):
    x = int(input(f'Input {i+1}: '))
    lst.append(x)

print(sorted(lst))
