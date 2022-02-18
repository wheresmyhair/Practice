#coding:utf-8
#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

a = input('Input: ')

print(f'Lenth: {len(a)}')
print(f'Reverse: {a[::-1]}')