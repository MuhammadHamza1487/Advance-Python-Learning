
# Python program to check if a string starts
# and ends with the same character
 
# import re module as it provides
# support for regular expressions 
import re
 
# the regular  expression
regex = r'^[A-Za-z0-9]$|^([A-Za-z0-9]).*\1$'
 
# function for checking the string
def check(string):
 
    # pass the regular expression 
    # and the string in the search() method 
    if(re.search(regex, string)):  
        print("Valid")  
    else:  
        print("Invalid")  
 
if __name__ == '__main__' :
 
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"
    sample4 = "AbcA"
    sample5 = "1bc1"
    sample6 = "AaaA"
 
    check(sample1)
    check(sample2)
    check(sample3)
    check(sample4)
    check(sample5)
    check(sample6)
    