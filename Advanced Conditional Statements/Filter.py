# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

# Python filter() Syntax
# The filter() method in Python has the following syntax:

# Syntax: filter(function, sequence)

# Parameters:

# function: function that tests if each element of a sequence is true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
# Returns: an iterator that is already filtered.

# _________________________________________________________________________________________________

# Python Filter Function with a Custom Function
# In this example, we are using the filter function along with a custom function “fun()” to filter out vowels from the Python List.


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r', 'a']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

# _________________________________________________________________________________________________

# Python filter() function is normally used with Lambda functions. In this example, we are using the lambda function to filter out the odd and even numbers from a list.

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

# _________________________________________________________________________________________________

# What does the filter() function do?
# The filter() function in Python filters elements from an iterable (like a list) based on a function (or None for truthy values). It returns an iterator that yields those elements for which the function returns True.

# _________________________________________________________________________________________________

# Using filter() with a lambda function:

# Example using filter() with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)  # Output: [2, 4, 6, 8]

# _________________________________________________________________________________________________

# Example filtering objects based on attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 22)
]
# Filter people older than 25
filtered_people = list(filter(lambda person: person.age > 25, people))
for person in filtered_people:
    print(person.name, person.age)
# _________________________________________________________________________________________________
