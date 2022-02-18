#coding:utf-8
#题目：利用递归方法求5!。

def fact(x):
    return fact(x-1)*x if x>1 else 1

fact(5)