#coding:utf-8
#题目：求一个3*3矩阵主对角线元素之和。

def trace(mat):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][i]
    return sum

a = [[1,2,3],[3,4,5],[5,4,2]]

trace(a)