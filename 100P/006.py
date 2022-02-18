#coding:utf-8
#题目：斐波那契数列。

# Init
upper = int(input('N='))
fibonacci = [0,1]

# Main
if upper<=0:
    print('Please check the input.')
elif upper==1:
    print(fibonacci[:1])
elif upper==2:
    print(fibonacci[:2])
else:
    for i in range(2,upper):
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    print(fibonacci)