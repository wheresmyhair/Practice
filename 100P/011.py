#coding:utf-8
#题目：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

import sys

month = int(input('Month(s)='))
print(f'Month(s) = {month}.')

if month<=0:
    sys.exit('Please check your input.')
if month==1 or month==2:
    sys.exit('2 rabbits total.')

month_1=1
month_2=0
month_3=0
month_elder=0

for i in range(month):
    month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
    print(f'Month: {i+1}, Couples: {month_1+month_2+month_3+month_elder}')
    print(f'Freshmen: {month_1} couples')
    print(f'Sophomore: {month_2} couples')
    print(f'Junior: {month_3} couples')
    print(f'Senior: {month_elder} couples')
    print('=======================================')

