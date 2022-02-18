#coding:utf-8
#题目：输入3个数a,b,c，按大小顺序输出。

x = []
for i in range(3):
    x.append(float(input(f'Input {i+1}: ')))

print(sorted(x))