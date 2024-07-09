
numbers = [12, 13, 14]
"""List of numbers"""

doubled = [x * 2 for x in numbers]
"""Create a new list with each number doubled using list comprehension"""

print(doubled)
"""Print the doubled list"""

# Syntax: newList = [ expression(element) for element in oldList if condition ] 

# Parameter:

# expression: Represents the operation you want to execute on every item within the iterable.
# element: The term “variable” refers to each value taken from the iterable.
# iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
# condition: (Optional) A filter helps decide whether or not an element should be added to the new list.
# Return:The return value of a list comprehension is a new list containing the modified elements that satisfy the given criteria.

# ---And same for that if we want to squared the number---
squared = [x ** 2 for x in numbers] 

# _________________________________________________________________________________________________

# In this example, we are assigning 1, 2, and 3 to the list and we are printing the list using List Comprehension.

List = [character for character in [1, 2, 3]] 
"""Using list comprehension to iterate through loop """

print(List)
"""Displaying list"""

# _________________________________________________________________________________________________

# In this example, we are printing the even numbers from 0 to 10 using List Comprehension.
list = [i for i in range(11) if i % 2 == 0] 
print(list)

# _________________________________________________________________________________________________

# In this example, we are assigning integers 0 to 2 to 3 rows of the matrix and printing it using List Comprehension.
matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)

# _________________________________________________________________________________________________

# List Comprehensions vs For Loop

List = []
for character in 'Rigrex': 
    List.append(character) 
print(List)

# Using list comprehension to iterate through loop 
List = [character for character in 'Rigrex'] 

# _________________________________________________________________________________________________

# Nested List Comprehensions are list comprehension within another list comprehension which is quite similar to nested for loops. Below is the program which implements nested loop:
matrix = [] 

for i in range(3):   
    # Append an empty sublist inside the list 
    matrix.append([]) 
    for j in range(5): 
        matrix[i].append(j) 
print(matrix)


# Now by using nested list comprehensions, the same output can be generated in fewer lines of code.
# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(3)] 
print(matrix) 

# _________________________________________________________________________________________________

#  Now here, we have used only list comprehension to display a table of 10.
numbers = [i*10 for i in range(1, 11)] 
print(numbers) 

# _________________________________________________________________________________________________

# Python List Comprehension using If-else.
lis = [f"{i}: Even number" if i % 2 == 0
	else f"{i}: Odd number" for i in range(8)] 
print(lis) 

# _________________________________________________________________________________________________

# Nested IF with List Comprehension
lis = [num for num in range(100) 
	if num % 5 == 0 if num % 10 == 0] 
print(lis)

# _________________________________________________________________________________________________

# In this example, we are making a transpose of the matrix using list comprehension.
# Assign matrix 
twoDMatrix = [[10, 20, 30], 
			[40, 50, 60], 
			[70, 80, 90]] 

# Generate transpose 
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))] 
print(trans) 

# _________________________________________________________________________________________________

# Reverse each string in a Tuple
# In this example, we are reversing strings in for loop and inserting them into the list, and printing the list.
List = [string[::-1] for string in ('Rigrex', 'Company')] 
# Display list 
print(List) 

# _________________________________________________________________________________________________

# Creating a list of Tuples from two separate Lists
# In this example, we have created two lists of names and ages. We are using zip()  in list comprehension and we are inserting the name and age as a tuple to list. Finally, we are printing the list of tuples.
names = ["Ali", "Akram", "Usman"] 
ages = [25, 30, 35] 
person_tuples = [(name, age) for name, age in zip(names, ages)] 
print(person_tuples)

# _________________________________________________________________________________________________

# Display the sum of digits of all the odd elements in a list.
# In this example, We have created a list and we are finding the digit sum of every odd element in the list.

# Explicit function 
def digitSum(n): 
	dsum = 0
	for ele in str(n): 
		dsum += int(ele) 
	return dsum 

# Initializing list 
List = [367, 111, 562, 945, 6726, 873] 
# Using the function on odd elements of the list 
newList = [digitSum(i) for i in List if i%2==1] 
# Displaying new list 
print(newList) 

# _________________________________________________________________________________________________


