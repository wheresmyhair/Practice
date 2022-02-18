#coding:utf-8
#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def rev(string):
    if len(string)!=1:
        rev(string[1:])
    print(string[0],end='')

rev('school')