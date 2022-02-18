#coding:utf-8
#题目：将一个列表的数据复制到另一个列表中。

import copy
a = [1,2,3,4,['a','b']]

# ASSIGN: 
#   If a changes at some point, b will also change (totally) after that change.
b = a

# SHALLOW COPY: 
#   If both objects and subobjects in a change, only subobjects will change. 
#   Objects in c will remain the same.
#   i.e., shallow copy will copy the object.
c = a[:] 
d = copy.copy(a)

# DEEP COPY: 
#   Can be interpreted as save. All of the objects and subobjects are saved.
e = copy.deepcopy(a)

a.append(5)
a[4].append('c')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)