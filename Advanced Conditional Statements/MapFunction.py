# Python map() function
# Last Updated : 05 Jul, 2024
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# Python map() Function Syntax
# Syntax : map(fun, iter)

# Parameters:

# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.
# NOTE: You can pass one or more iterable to the map() function.

# Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# _________________________________________________________________________________________________

# Add Two Lists Using map and lambda
# In this example, we are using map and lambda to add two lists.


# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# _________________________________________________________________________________________________

# Modify` the String using map()
# In this example, we are using map() function to modify the string. We can create a map from an iterable in Python.

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
# _________________________________________________________________________________________________
