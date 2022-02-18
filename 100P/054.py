#coding:utf-8
#题目：位取反、位移动: 取一个整数a从右端开始的4~7位。

# x = input('Input: ')
# print(x[::-1][3:7])

a=int(input('输入一个数字: '))
b=0                 #     0
b=~b                #     1
b=b<<4              # 10000
b=~b                #  1111
c=a>>4
d=c&b
print('a:',bin(a))
print('b:',bin(b))
print('c:',bin(c))
print('d:',bin(d))