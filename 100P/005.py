#coding:utf-8
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

lst = []
for i in range(3):
    x = int(input('int%d: '%(i)))
    lst.append(x)

print(sorted(lst))

