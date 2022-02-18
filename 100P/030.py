#coding:utf-8
#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

a = input('Input: ')

b = a[::-1]
if b==a:
    print('Yes')
else:
    print('No')
