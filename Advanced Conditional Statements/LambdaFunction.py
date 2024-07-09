# Python lambda
# In Python, an anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

# Python lambda Syntax:
# lambda arguments : expression

# Example:
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))

# Python lambda properties:
# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
# It has various uses in particular fields of programming, besides other types of expressions in functions.

# _________________________________________________________________________________________________
# Example 1: Program to demonstrate return type of Python lambda keyword 

string = 'RigrexComapny'
 
# lambda returns a function object
print(lambda string: string)

# Output: <function <lambda> at 0x000001B43331D300>:
#       Explanation: In this above example, the lambda is not being called by the print function, but simply returning the function object and the memory location where it is stored. So, to make the print to print the string first, we need to call the lambda so that the string will get pass the print.
# _________________________________________________________________________________________________

# Invoking lambda return value to perform various operations
# Here we have passed various types of arguments into the different lambda functions and printed the result generated from the lambda function calls.


filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Rigrex101"))
 
do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))
 
find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

# _________________________________________________________________________________________________
# Difference between lambda and normal function call
# The main difference between lambda function and other functions defined using def keyword is that, we cannot use multiple statements inside a lambda function and allowed statements are also very limited inside lambda statements. Using lambda functions to do complex operations may affect the readability of the code.


def cube(y):
    return y * y * y
print("invoking function defined with def keyword:", cube(30))
 
lambda_cube = lambda num: num ** 3
print("invoking lambda function:", lambda_cube(30))

# _________________________________________________________________________________________________

# The lambda function gets more helpful when used inside a function.
# We can use lambda function inside map(), filter(), sorted() and many other functions. Here, we have demonstrated how to use lambda function inside some of the most common Python functions.


l = ["1", "2", "9", "0", "-1", "-2"]

# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(l, key=lambda x: int(x)))
 
# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
      list(filter(lambda x: (int(x) % 2 == 0 and int(x) > 0), l)))
 
# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), l)))
# _________________________________________________________________________________________________
