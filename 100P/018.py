#coding:utf-8
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

import sys

a = input('a=')
if float(a)<1 or float(a)>9:
    sys.exit('Check input.')
n = int(input('n='))

lst = []

for i in range(1,n+1):
    lst.append(int(a*i))

print(lst)
print(sum(lst))