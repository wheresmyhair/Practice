#coding:utf-8
#题目：求输入数字的平方，如果平方运算后小于 50 则退出。

# This will return 'Check input.' and continue for the next input.
while True:
    try:
        x = float(input('Input: '))
    except:
        print('Check input.')
        continue
    print(x**2)
    if x**2<50:
        break

# This will return python error info and exit.
while True:
    x = float(input('Input: '))
    print('Check input.')
    print(x**2)
    if x**2<50:
        break
