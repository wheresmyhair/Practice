# Filter items out of a sequence
# Return filtered list
# [m, n, p] -> filter function -> [m, n]

# Pick out elements which are larger than 2
n = [4,3,2,1]

# Traditional approach
def over2(lst):
    cache_lst = []
    for i in lst:
        if i>2:
            cache_lst.append(i)
    return cache_lst

over2(n)

# List comprehension
def over2_new(lst):
    return [x for x in lst if x>2]
over2_new(n)


[x for x in n if x>2]


# Filter approach
# filter(condition, obj)
# If condition holds, bring out the obj
list(filter(lambda x: x>2, n))
