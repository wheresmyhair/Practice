#coding:utf-8
#题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

lst = [1,3,5,6,7,8,9,2]
lst[lst.index(max(lst))], lst[0] = lst[0], lst[lst.index(max(lst))]
lst[lst.index(min(lst))], lst[-1] = lst[-1], lst[lst.index(min(lst))]
print(lst)