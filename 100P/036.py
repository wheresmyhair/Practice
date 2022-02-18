#coding:utf-8
#题目：求100之内的素数。

lst = []
def isPrime(x):
    if not isinstance(x,int):
        return 'Input should be an integer.'
    if x==1:
        return False
    elif x<1:
        return 'Check input.'
    else:
        for i in range(2,round(x**0.5)+1):
            if x%i==0:
                return False
        return True

for i in range(1,100):
    if isPrime(i):
        lst.append(i)

print(lst)