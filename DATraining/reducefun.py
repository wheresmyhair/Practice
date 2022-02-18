from functools import reduce
# [m, n, p] -> reduce -> f(f(m, n), p)

# Multiply them together
n = [4,3,2,1]

# Traditional approach
def mult(lst):
    cache_prod = lst[0]
    for i in range(1,len(lst)):
        cache_prod *= lst[i]
    return cache_prod

mult(n)

# Reduce approach
reduce(lambda x,y:x*y, n)