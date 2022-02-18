# Apply same function to each element of a sequence
# Return the modified list
# [m, n, p] -> map function -> [f(m), f(n), f(p)]

# Square each elem in the list
n = [4,3,2,1]

# Traditional approach:
def sqr(lst):
    cache_lst = []
    for i in lst:
        cache_lst.append(i**2)
    return cache_lst

def sqr_old(lst):
    cache_lst = []
    for i in range(len(lst)):
        cache_lst.append(lst[i]**2)
    return cache_lst

sqr(n)
sqr_old(n)

# Map approach:
list(map(lambda x:x**2, n))

# List comprehension solution
[x**2 for x in n]
