#coding:utf-8
#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = float(input('Score: '))
print('A' if score>=90 else ('C' if score<=60 else 'B'))