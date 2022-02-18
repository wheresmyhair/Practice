#coding:utf-8
#题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

lst = ['Monday','Tuesday','Wednesday','Thursday','Firday','Saturday','Sunday']

a1 = input("First Char: ")
lst2 = []
for i in range(len(lst)):
    if a1==lst[i][0]:
        lst2.append(lst[i])

if len(lst2)==1:
    print(lst2[0])
else:
    a2 = input("Second Char: ")
    for i in range(len(lst2)):
        if a2==lst2[i][1]:
            print(lst2[i])
