# Simple uses
def doublenum(x):
    return x*2

a = lambda x: x*2

a(3)

def addnum(x,y):
    return x+y

lambda x,y: x+y

a = lambda x,y: x+y

a(1,2)


# Sorting a list of tuples using lambda
lst = [('eggs',5.25), ('honey', 1.23), ('banana', 3), ('apple', 1)]
# This will sort the original list
lst.sort(key=lambda x: x[0])
# This will return a sorted list, leaving the original list untouched
sorted(lst, key=lambda x:x[0])


# Sorting a list of dictionaries using lambda
lst = [
    {'make':'Ford', 'model':'A','year':2021},
    {'make':'Tesla', 'model':'F','year':2020},
    {'make':'BMW', 'model':'X','year':2019}
    ]
# Sort with desc (default is asc so need argument reverse=True)
lst.sort(key=lambda x: x['model'], reverse=True)


# Filtering a list of integers using lambda
# Find even numbers
lst = [1,2,3,4,5,6]
list(filter(lambda x: x%2==0,lst))
[x for x in lst if x%2==0]


# Lambda conditionals
# Find list elements that start with Upper A
lst = ['Apple', 'Abandon', 'absolute', 'Banana', 'big']
# Notice: startswith() is case sensitive
starts_with_A = lambda x: True if x.startswith('A') else False
list(map(starts_with_A,lst))

# Find the word before the given word
# .index('big') returns the position of 'big'
wordbefore = lambda s,w: s.split()[s.split().index(w)-1] if w in s else None
sentence = "I love you so much"
wordbefore(sentence, 'much')


# Lambda datetime objects
import datetime
now = datetime.datetime.now()
year = lambda x: x.year
year(now)


