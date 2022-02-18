####################################
#            Sequences             #
####################################
#   String, list, tuple
#   String
x = 'apple'
x[0]
#   List
x = ['pig', 'cow', 'cat']
x[0]
#   Tuple
x = ('1','2')
x[1]

# Slicing 
x = 'computer'
# [start:end+1:step]
x[0:6:2]
# Last item
x[-1]
# Second last item
x[-2]
# All except last 2 items
x[:-2]
# Last 2 items
x[-2:]

# Adding/concatenating
x = 'horse' + 'shoe'
x

# Multiplying
x = 'bug' * 3
x
x = [6,3] * 3
x

# Checking membership
x = 'bug'
'u' in x
x = ['bug', 'apple', 'cow']
'bugs' in x

# Iterating
# If we only need items
x = [2,3,4]
for i in x:
    print(i**2)
# If we need the indcies and the items
for i,j in enumerate(x):
    print(i,j)
# To make things clear, better not to use i,j
for index, item in enumerate(x):
    print(index, item)

# Minimum/Maximum (alpha numeric types, but cannot mix types)
x = 'apple'
min(x)
max(x)
x = ['cow', 'cat', 'apple', 'banana']
min(x)
max(x)

# Sorting
x = 'bug'
sorted(x)

# Count (item)
x = 'apple'
x.count('p')

# Index (item)
x.index('p')

# Unpacking
# Must exactly match!
x = 'apple'
a,b,c,d,e = x
x = ['banana','orange','apple']
a,b,c = x


####################################
#              Lists               #
####################################
# List comprehension
#   Create a new list use what returned in the for loop
x = [m for m in range(5)]
x
x = [z**2 for z in range(10) if z>4]
x

# Delete
del(x[0])
x
del(x)

# Append
x = [1,2,3]
x.append(4)
x

# Extend
x = [1,2,3]
y = [4,5]
# Pay attention to the difference!
x.append(y)
# Returns [1, 2, 3, [4, 5]]
x.extend(y)
x+y
# Returns [1, 2, 3, 4, 5]

# Insert (index,item)
x = [1,2,3,5]
x.insert(3,4)
x
x.insert(0,['a','b'])
x

# Pop
#   Pops the last item OFF the list, and returns the item
x = [1,2,3,4,5]
x.pop()
x

# Remove
#   Remove the first instance of an item
#   remove(...) is not the index! If want to remove elements by indcies, use del(...) instead
x = [1,2,3,4,5,6,4]
x.remove(4)
x

# Reverse
x = [1,2,3,4,5]
x.reverse()
x


#############################
#           Tuples          #
#############################
x = (1,2,3)
x = 1,2,3
x = 1, # The comma is necessary.
x = ()

x = [1,2,3,4]
x = tuple(x)

x[0] = 1 # Error!

x = ([1,2],3)
del(x[0]) # Error!
del(x[0][1]) # But you can change the list elements inside of a tuple



#############################
#            Sets           #
#############################
x = {3,4,3,5} # Returns {3,4,5}
x = set()
x = {}
x = [1,2,3,4,4]
x = set(x) # Set from a list

# Set comprehension
x = {3*m for m in range(10) if m>3}

# Basic set operations
x.add(3)
x.remove(15)
len(x)
3 in x
x.pop() # Notice, since set is unordered, we don't know which one will be popped before we do pop()
x.clear() # Delete all items from set x

# Stardard mathematical set operations
x = {1,2,3}
y = {3,4,5,6}
x & y # And
x | y # Or
x ^ y # Xor
x - y # In x but not in y
x <= y # y contains x
x >= y # x contains y



#############################
#       Dictionaries        #
#############################
# Construct a dict
x = {'pork':20, 'beef':30, 'chicken':40}
x = dict([('pork',20),('beef',30),('chicken',40)])
x = dict(pork=20,beef=30,chicken=40)

# Basic operations
x['beef']
del x['beef']
'chicken' in x # Cannot check values!
x.clear()

# Accessing keys and values
x.keys()
x.values()
x.items() # Return tuple pairs in x
30 in x.values() # Check values in this way!

# Iterating
for k in x:
    print(k,x[k])
# Preferred approach
for k,v in x.items():
    print(k,v)