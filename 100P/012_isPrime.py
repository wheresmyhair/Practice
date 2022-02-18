#coding:utf-8
#题目：判断101-200之间有多少个素数，并输出所有素数。

def isPrime(x):
    if x<=0:
        return 'Check input.'
    if x==1:
        return False
    for i in range(2,round(x**0.5)+1):
        if x%i==0:
            return False
    return True
    
lst = []

for i in range(101,201):
    if isPrime(i):
        lst.append(i)

print(f'Number of primes in (101,200): {len(lst)}')
print(lst)

