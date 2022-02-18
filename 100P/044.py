#coding:utf-8
#题目：计算两个矩阵相加。

def matadd(mata,matb):
    cache = [[0 for i in range(len(mata[0]))] for j in range(len(mata))]
    for i in range(len(mata)):
        for j in range(len(mata[0])):
            cache[i][j] = (mata[i][j]+matb[i][j])
    return cache


a = [[1,2,],[3,4,]]
b = [[1,2,],[3,4,]]

matadd(a,b)