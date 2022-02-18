#coding:utf-8
#题目：打印出如下图案（菱形）:  
# *    ***   *****  *******   *****    ***     *

for i in range(-3,4):
    n = abs(i)
    print(" "*n + "*"*(7-2*n))