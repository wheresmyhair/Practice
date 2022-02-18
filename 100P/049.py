#coding:utf-8
#题目：使用lambda来创建匿名函数。

mmin = lambda x,y: x if x<=y else y
mmax = lambda x,y: x if x>=y else y

# Alternative approach
Max=lambda x,y:x*(x>=y)+y*(y>x)
Min=lambda x,y:x*(x<=y)+y*(y<x)

print(mmax(1,2))
print(mmin(1,2))