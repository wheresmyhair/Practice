#coding:utf-8
#题目：输入某年某月某日，判断这一天是这一年的第几天？


def isLeapYear(x):
    return ((x%4==0 and x%100!=0) or x%400==0)

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("day: "))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
whichday = 0

for i in range(0,month):
    if i == month-1:
        whichday += day
    else:
        whichday += days[i]

if isLeapYear(year) and month>2:
    whichday += 1

print(whichday)

