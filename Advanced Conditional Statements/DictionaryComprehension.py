# Python Dictionary Comprehension Example
# Here we have two lists named keys and value and we are iterating over them with the help of zip() function.

# Python code to demonstrate dictionary 
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)} 

# We can use below too
# myDict = dict(zip(keys, values)) 
print (myDict)

# _________________________________________________________________________________________________

# Using fromkeys() Method
# Here we are using the fromkeys() method that returns a dictionary with specific keys and values.
dic=dict.fromkeys(range(5), False)
print(dic)

# _________________________________________________________________________________________________

# Python code to demonstrate dictionary 
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

# _________________________________________________________________________________________________

sDict = {x.upper(): x*3 for x in 'coding'}
print (sDict)

# _________________________________________________________________________________________________

# We can use Dictionary comprehensions with if and else statements and with other expressions too. This example below maps the numbers to their cubes that are not divisible by 4.
# Python code to demonstrate dictionary 
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

# _________________________________________________________________________________________________

# Using nested dictionary comprehension
# Here we are trying to create a nested dictionary with the help of dictionary comprehension.

# given string
l="GFGGF"
# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}
print(dic)

# _________________________________________________________________________________________________